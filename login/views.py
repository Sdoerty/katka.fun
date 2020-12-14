from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib import messages
from django.contrib.auth import login, logout


def user_login(request):
    if request.POST == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('mainpage')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})



