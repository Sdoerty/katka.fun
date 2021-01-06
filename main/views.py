from django.shortcuts import render
from django.views.generic import DetailView

from .models import Katka


def index(request):
    ktk = Katka.objects.all()
    return render(request, 'main/main.html', {"ktk": ktk})


def katka_page(request, pk):
    ktk_item = Katka.objects.get(pk=pk)
    return render(request, 'katka_page/katka_page.html', {"ktk_item": ktk_item})


def create_katka(request):
    return render(request, 'create_katka/create_katka.html')
