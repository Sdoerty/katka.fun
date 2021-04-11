from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .forms import AccountAuthenticationForm


def user_login(request, *args, **kwargs):
    context = {}

    # user = request.user
    # if user.is_authenticated:
    #     return redirect("main")

    destination = get_redirect_if_exists(request)
    print("destination: " + str(destination))

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                if destination:
                    return redirect(destination)
                return redirect("main")

    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form

    return render(request, 'login.html', {"form": form})


def get_redirect_if_exists(request):
    redirect = None
    if request.GET:
        if request.GET.get("next"):
            redirect = str(request.GET.get("next"))
    return redirect


def logout_view(request):
    logout(request)
    return redirect('login')
