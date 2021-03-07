from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .forms import KatkaForm, KatkaEntryForm
from .models import Katka
from django.db import connection


def index(request):
    ktk = Katka.objects.all()
    return render(request, 'main/main.html', {"ktk": ktk})


def katka_page(request, pk):
    ktk_item = Katka.objects.get(pk=pk)

    if request.method == 'POST':
        # form = Katka.objects.raw("UPDATE main_katka SET members = format('%s,%s', members, 100) WHERE id = 13")
        # form.save()
        enter_katka(self=pk)
        return redirect('main')

    return render(request, 'katka_page/katka_page.html', {"ktk_item": ktk_item})


def enter_katka(self):
    with connection.cursor() as cursor:
        cursor.execute("UPDATE main_katka SET descr=123 WHERE id=13")
        row = cursor.fetchone()
    return row


def create_katka(request):
    poster = request.user

    if request.method == 'POST':
        form = KatkaForm(data=request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = poster
            form.save()
            return redirect('main')
        else:
            print(form.errors)
    else:
        form = Katka()

    return render(request, 'create_katka/create_katka.html', {'form': form})
