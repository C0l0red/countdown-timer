from django.contrib import messages, auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from app.models import Timer
from .forms import TimerForm


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('show_timers')
        else:
            print(form.errors)

    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.info(request, "Username already taken")
            return redirect('signup')
        else:
            user = User.objects.create_user(username=username,
                                            password=password)
            print(user)
            print("User registered Successfully")
            user.save()
            return redirect('login')
    else:
        return render(request, 'signup.html')


def logout(request):
    auth.logout(request)
    return redirect('show_timers')


def show_timers(request):
    timers = Timer.objects.filter(user=request.user).order_by('priority')
    form = TimerForm()

    if len(timers) == 0:
        return render(request, 'show_timers.html', {
            'form': form,
            'editable': False,
            'timers': None,
        })

    return render(request, 'show_timers.html', {
        'form': form,
        'editable': False,
        'timers': timers,
    })


def add_timer(request):
    editable = True
    if request.method == "POST":
        editable = False
        form = TimerForm(request.POST)
        if form.is_valid():
            form_instance = form.save(commit=False)
            form_instance.user = request.user
            form_instance.save()
            return redirect("show_timers")
    else:
        form = TimerForm()
        timers = Timer.objects.all()
        return render(request, 'show_timers.html', {
            'form': form,
            "editable": editable,
            'timers': timers
        })
