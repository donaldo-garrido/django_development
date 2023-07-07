from django.shortcuts import render
from django.http import Http404
from django.views.generic import DetailView, ListView

from .models import Notes
# Create your views here.

class NotesListView(ListView):
    model = Notes
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'

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