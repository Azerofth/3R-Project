from django.shortcuts import render, redirect
from .models import *

from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .forms import SignupForm, LoginForm

# Create your views here.


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                auth_login(request, user)
                print(f"Welcome, {username}")
                
                return redirect('main')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('home')

def home(request):
    return render(request, 'home.html')

def registration(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        print(form)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            new_user1 = User.objects.create_user(
                    username=username,
                    password=password,  
                )
            new_user1.save()
            return redirect('login')
    else:
        form = SignupForm()
        print(form)
    return render(request, 'registration.html', {'form': form})

def main(request):
    return render(request, 'main.html')

             






            
