from django.shortcuts import render, redirect
from .forms import RegForm
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('user_profile')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = RegForm()

    return render(request, 'signup.html', {"form": form})
