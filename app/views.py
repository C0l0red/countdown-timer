from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from app.models import Timer
from .forms import PomodoroForm


def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=email).exists():
            user = auth.authenticate(username=email, password=password)
            print(user)
            if user is not None:
                auth.login(request, user)
                return redirect('show_timers')
            else:
                messages.error(request, 'Invalid credentials')
                return redirect("login")
        else:
            messages.info(request, "Invalid email or password")
            return redirect('login')
    else:
        return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        name = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(first_name=name).exists():
            messages.info(request, "Username already taken")
            return redirect('signup')
        elif User.objects.filter(username=email).exists():
            messages.info(request, "Email already taken")
            return redirect('signup')
        else:
            user = User.objects.create_user(first_name=name,
                                            username=email,
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
    timers = Timer.objects.all().order_by('priority')
    form = PomodoroForm()

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


def add(request, id: int):
    editable = True
    if request.method == "POST":
        editable = False
        form = PomodoroForm(request.POST)
        if form.is_valid():
            form_instance = form.save(commit=False)
            form_instance.uuid = id
            form_instance.save()
            return redirect("show_timers")
    else:
        form = PomodoroForm()
        timers = Timer.objects.all()
        return render(request, 'show_timers.html', {
            'form': form,
            "editable": editable,
            'timers': timers
        })

