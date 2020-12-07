from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import RegForm


def login(request):
    # if request.method == 'POST':
    #     form = RegForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('mainpage')
    # else:
    #     form = RegForm()

    return render(request, 'account/login.html')
