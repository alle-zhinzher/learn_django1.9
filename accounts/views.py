from django.contrib.auth import (
                authenticate,
                get_user_model,
                login,
                logout,
)
from django.shortcuts import render, redirect

from .forms import UserLoginForm, UserRegisterForm


def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        print(request.user.is_authenticated)
        if next:
            return redirect(next)
        return redirect('/')
    return render(request, 'login_form.html', context={'form': form})


def logout_view(request):
    logout(request)
    return render(request, 'login_form.html', {})


def register_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        passwaord = form.cleaned_data.get('password')
        user.set_password(passwaord)
        user.save()
        new_user = authenticate(username=user.username, passwaord=passwaord)
        login(request, user)
        print(request.user.is_authenticated)
        if next:
            return redirect(next)
        return redirect('/')
    return render(request, 'register_form.html', context={'form': form})
