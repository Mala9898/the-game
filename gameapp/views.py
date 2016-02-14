from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth

from . import forms, models

def index(request):
    return render(request, 'home.html', {'user': request.user})

def login(request):
    # if this is a POST request we need to process the form data
    bad_login = False
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect("/")
            else:
                bad_login = True
    else:
        form = forms.LoginForm()

    return render(request, 'login.html', {'form': form, 'bad_login': bad_login})

def register(request):
    # if this is a POST request we need to process the form data
    bad_username = False
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            if models.User.objects.filter(username=username).first() is not None:
                bad_username = True
            else:
                user = models.User.objects.create_user(username=username, password=password)
                user = auth.authenticate(username=username, password=password)
                auth.login(request, user)
                return HttpResponseRedirect("/")
    else:
        form = forms.LoginForm()

    return render(request, 'register.html', {'form': form, 'bad_username': bad_username})

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
    return HttpResponseRedirect("/")
