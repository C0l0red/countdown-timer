from django.shortcuts import render, redirect
from django.utils import timezone

from app.models import Timer
from .forms import PomodoroForm


def show_timers(request):
    timers = Timer.objects.all()
    form = PomodoroForm()

    if len(timers) == 0:
        return render(request, 'countdown_timer.html', {
            'form': form,
            'editable': False,
            'timers': None,
        })

    return render(request, 'countdown_timer.html', {
        'form': form,
        'editable': False,
        'timers': timers,
    })


def add(request, id: int):
    editable = True
    if request.method == "POST":
        editable = False
        form = PomodoroForm(request.POST)
        if form.is_valid():
            form_instance = form.save(commit=False)
            form_instance.uuid = id
            form_instance.save()
            return redirect("timers")
    else:
        form = PomodoroForm()
        timers = Timer.objects.all()
        return render(request, 'countdown_timer.html', {
            'form': form,
            "editable": editable,
            'timers': timers
        })

