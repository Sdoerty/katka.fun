from django.shortcuts import render


def index(request):
    return render(request, 'main/main.html')


def katka_page(request):
    return render(request, 'katka_page/katka_page.html')


def create_katka(request):
    return render(request, 'create_katka/create_katka.html')
