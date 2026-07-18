from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import RegisterForm


def home(request):
    return render(request, 'accounts/home.html')


def register(request):

    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created successfully!")
            return redirect('dashboard')

    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})


def user_login(request):

    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Logged in successfully!")
            return redirect('dashboard')

        messages.error(request, "Invalid username or password.")

    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})


@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html')


@login_required
def user_logout(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('login')