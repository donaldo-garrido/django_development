from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseRedirect

from .forms import NotesForm
from .models import Notes
# Create your views here.

class NotesCreateView(CreateView):
    model = Notes # Know what model we are talking about
    #fields = ['title', 'text']
    success_url = '/smart/notes' # Redirect the user to the list of notes, to let him/her see the note created.
    form_class = NotesForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NotesUpdateView(UpdateView):
    model = Notes # Know what model we are talking about
    success_url = '/smart/notes' # Redirect the user to the list of notes, to let him/her see the note created.
    form_class = NotesForm

class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name = 'notes/notes_delete.html'



class NotesListView(ListView, LoginRequiredMixin):
    model = Notes
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'
    login_url = "/admin"

    def get_queryset(self):
        return self.request.user.notes.all()
#def list(request):
#    all_notes = Notes.objects.all() #Stores all the notes
#    return render(request, 'notes/notes_list.html', {'notes': all_notes})


class NotesDeatilView(DetailView):
    model = Notes
    context_object_name = 'note'

def detail(request, pk):
    

    try:
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404("Note doesn't exist")
    return render(request, 'notes/notes_detail.html', {'note':note})