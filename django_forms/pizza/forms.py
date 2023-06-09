from django import forms
from .models import Pizza, Size

"""class PizzaForm(forms.Form):
    topping1 = forms.CharField(label='Topping 1', max_length=100)
    topping2 = forms.CharField(label='Topping 2', max_length=100)
    #toppings = forms.MultipleChoiceField(choices=[('pep','Pepperoni'), ('cheese', 'Cheese'), ('olives', 'Olives')], widget=forms.CheckboxSelectMultiple)
    size = forms.ChoiceField(label='Size', choices=[('Small','Small'), ('Medium', 'Medium'), ('Large', 'Large')])"""


class PizzaForm(forms.ModelForm):

    #email = forms.EmailField()
    #url = forms.URLField()

    #size = forms.ModelChoiceField(queryset=Size.objects, empty_label=None, widget=forms.RadioSelect)
    #image = forms.ImageField()

    class Meta:
        model = Pizza
        fields = ['topping1', 'topping2', 'size']
        labels = {'topping1':'Topping 1', 'topping2':'Topping 2', 'size':'Size'}
        #widgets = {'topping1': forms.Textarea, 'size': forms.CheckboxSelectMultiple}

class MultiplePizzaForm(forms.Form):
    number = forms.IntegerField(min_value=2, max_value=6)







#    <label for="topping1">Topping 1: </label>
#    <input id="topping1" type="text" name="topping1">
#    <label for="topping2">Topping 2: </label>
#    <input id="topping2" type="text" name="topping2">
#    <label for="size">Size: </label>
#    <select id="size" name="size">
#        <option value="Small">Small</option>
#        <option value="Medium">Medium</option>
#        <option value="Large">Large</option>
#    </select>