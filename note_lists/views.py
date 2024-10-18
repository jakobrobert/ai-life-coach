from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from .models import NoteList, Note


def note_lists(request):
    note_lists = NoteList.objects.all()
    return render(request, 'note_lists.html', {'note_lists': note_lists})


@require_POST
def add_note_list(request):
    title = request.POST.get('title')
    NoteList.objects.create(title=title)
    return redirect('note_lists')


def note_list(request, pk):
    note_list = get_object_or_404(NoteList, pk=pk)
    return render(request, 'note_list.html', {'note_list': note_list})


@require_POST
def add_note(request, pk):
    title = request.POST.get('title')
    text = request.POST.get('text')
    note_list = get_object_or_404(NoteList, pk=pk)
    Note.objects.create(title=title, text=text, note_list=note_list)
    return redirect('note_list', pk=pk)


# TODO require delete?
def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    note_list_id = note.note_list.id
    note.delete()
    return redirect('note_list', pk=note_list_id)
