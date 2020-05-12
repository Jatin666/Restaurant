from django.shortcuts import render, redirect
from . import forms
from . import models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.

def register(request):
    form = forms.Register()
    error = None
    if request.method == "POST":
        form = forms.Register(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if len(data['username']) < 4 or len(data['password']) < 4:
                error = "The length of the username or password is too short"
            elif models.UserDetails.objects.filter(username=data['username']).exists():
                error = "The username already exists in the database"
            elif models.UserDetails.objects.filter(email=data['email']).exists():
                error = "The email already exists in the database"
            if error is None:
                data['password'] = make_password(data['password'])
                ud = models.UserDetails(**data)
                ud.save()
                print("Saved")
    return render(request, 'details/register.html', {'form': form, 'error': error})


def signin(request):
    error = None
    if request.user.is_authenticated:
        error = "Logged in already"
    form = forms.Login()
    if request.method == "POST":
        form = forms.Login(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            user = authenticate(request, username=data['username'], password=data['password'])
            print(user)
            if user is not None:
                login(request, user)
                error = "Successful Login"
            else:
                error = "The username or password is wrong"
    return render(request, 'details/login.html', {'form': form, 'error': error})