from django.shortcuts import render, redirect
from .forms import KatkaLoginForm


def login(request):
    if request.method == 'POST':
        form = KatkaLoginForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
    else:
        form = KatkaLoginForm()

    return render(request, 'account/login.html')


