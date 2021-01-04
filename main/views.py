from django.shortcuts import render
from .models import Katka


def index(request):
    return render(request, 'main/main.html')


def katka_page(request):
    ktk = Katka.objects.all()
    return render(request, 'katka_page/katka_page.html', {"ktk": ktk})


def create_katka(request):
    return render(request, 'create_katka/create_katka.html')
