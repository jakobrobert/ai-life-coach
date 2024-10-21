from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.decorators.http import require_POST

from .models import NoteList, Note


def get_note_lists(request):
    note_lists = NoteList.objects.all()
    return render(request, 'note_lists.html', {'note_lists': note_lists})


@require_POST
def add_note_list(request):
    title = request.POST.get('title')
    NoteList.objects.create(title=title)
    return redirect('get_note_lists')


def get_note_list(request, note_list_id):
    note_list = get_object_or_404(NoteList, id=note_list_id)
    report = request.GET.get('report', '')

    context = {
        'note_list': note_list,
        'report': report,
    }

    return render(request, 'note_list.html', context)


def delete_note_list(request, note_list_id):
    note_list = get_object_or_404(NoteList, id=note_list_id)
    note_list.delete()
    return redirect('get_note_lists')


@require_POST
def add_note(request, note_list_id):
    title = request.POST.get('title')
    text = request.POST.get('text')
    note_list = get_object_or_404(NoteList, id=note_list_id)
    Note.objects.create(title=title, text=text, note_list=note_list)
    return redirect('get_note_list', note_list_id=note_list_id)


def delete_note(request, note_list_id, note_id):
    note = get_object_or_404(Note, id=note_id)
    note.delete()
    return redirect('get_note_list', note_list_id=note_list_id)


@require_POST
def generate_report(request, note_list_id):
    # TODO Implement generate_report
    report = "In dieser Woche wurden die Projektziele erfolgreich festgelegt und die ersten Aufgaben abgeschlossen. Das Team arbeitet gut zusammen und ist bereit, die nächste Phase zu starten."
    return redirect(f"{reverse('get_note_list', args=[note_list_id])}?report={report}")
