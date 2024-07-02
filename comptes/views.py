from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import FormLogin, SignUpForm


def Form_view(request):
    form = FormLogin(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:  # si user n'est pas vide  
            login(request, user)
            return redirect("blog")
    return render(request, "comptes/login.html", {"form": form})

def Logout_view(request):
    logout(request)
    return redirect('index')

def Form_Sign(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password_raw = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            user = authenticate(username=username, password=password_raw)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, "comptes/register.html", {"form": form})