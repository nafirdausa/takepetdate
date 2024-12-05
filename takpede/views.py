from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import CustomUser
from .forms import CustomUserCreationForm


# Create your views here.

def index(request):
    return render(request, 'apps/index.html')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('find_match')
    else:
        form = CustomUserCreationForm()

    return render(request, 'apps/signup.html', {'form':form})

def signin(request):
    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('find_match')
        else:
            messages.error(request, 'Username atau Password salah')
    return render(request, 'apps/signin.html')

def update_profile(request):
    return render(request, 'apps/profile.html')
