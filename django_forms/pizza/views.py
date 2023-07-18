from django.shortcuts import render
from .forms import PizzaForm, MultiplePizzaForm
from django.forms import formset_factory
from .models import Pizza, Size
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.

def home(request):
    return render(request, 'pizza/home.html')

def order(request):
    multiple_form = MultiplePizzaForm()
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST)#, request.FILES)
        if filled_form.is_valid():
            created_pizza = filled_form.save()
            created_pizza_pk = created_pizza.id

            note = ' Your %s, %s and %s pizza is on its way' %(filled_form.cleaned_data['size'],
                                                            filled_form.cleaned_data['topping1'],
                                                            filled_form.cleaned_data['topping2'],)
            filled_form = PizzaForm()
        else:
            created_pizza_pk = None
            note = 'Pizza order has failed. Try again.'
        return render(request, 'pizza/order.html', {'created_pizza_pk':created_pizza_pk, 'pizzaform':filled_form, 'note':note, 'multiple_form':multiple_form})
    else:
        form = PizzaForm()
        return render(request, 'pizza/order.html', {'pizzaform':form, 'multiple_form':multiple_form})




def pizzas(request):
    number_of_pizzas = 2
    filled_multiple_pizza_form = MultiplePizzaForm(request.GET)
    if filled_multiple_pizza_form.is_valid():
        number_of_pizzas = filled_multiple_pizza_form.cleaned_data['number']

    PizzaFormSet = formset_factory(PizzaForm, extra=number_of_pizzas)
    formset = PizzaFormSet()
    if request.method == 'POST':
        filled_formset = PizzaFormSet(request.POST)
        if filled_formset.is_valid():
            for form in filled_formset:
                print(form.cleaned_data['topping1'])
            note = 'Pizzas have been ordered!'
        else: note = 'Order was not created, please try again'

        return render(request, 'pizza/pizzas.html', {'note':note, 'formset':formset})
    else:
        return render(request, 'pizza/pizzas.html', {'formset':formset})
    


def edit_order(request, pk):
    pizza = Pizza.objects.get(pk=pk)
    form = PizzaForm(instance=pizza)
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST, instance=pizza)
        if filled_form.is_valid():
            filled_form.save()
            form = filled_form
            note = 'Order has been updated'
            return render(request, 'pizza/edit_order.html', {'pizzaform':form, 'pizza':pizza, 'note':note})
    return render(request, 'pizza/edit_order.html', {'pizzaform':form, 'pizza':pizza})

# fetching pizzas and saving in a dictionary
@login_required(login_url='login')
def db(request):
    data = serializers.serialize('python', Pizza.objects.filter())
    #size_list = serializers.serialize('python', Size.objects.all())
    print(data)
    #print(size_list)
    dict_size = []
    """
    for sizex in size_list:
        id = sizex['pk']
        name = sizex['fields']['title']
        print(id)
        print(name)

        dict_size[id] = name

    """

    

    x = Pizza.objects.all()
    aux = 0

    for obj in x:
        print(x[aux].size.title)
        print(x[aux].topping1)
        print(x[aux].topping2)

        dict_size.append({'topping1':x[aux].topping1, 'topping2':x[aux].topping2, 'size':x[aux].size.title})

        aux += 1
    print(dict_size)

    context = {'dict_size':dict_size}
    #print(x.fields.size.title)
    return render(request, 'pizza/db.html', context)


#def authorized(request):
#    return render(request, 'pizza/authorized.html', {})

class LoginInterfaceView(LoginView):
    template_name = 'pizza/login.html'

class LogoutInterfaceView(LogoutView):
    template_name = 'pizza/logout.html'