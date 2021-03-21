from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .forms import KatkaForm, KatkaEntryForm
from .models import Katka
from django.db import connection
from django.contrib.auth.models import User
from profile.models import Profile


def index(request):
    ktk = Katka.objects.all()
    return render(request, 'main/main.html', {"ktk": ktk})


def katka_page(request, pk):
    '''
    ktk_item получаем все обьекты каток по идентификатору. Глобальный потому что только так можно его использовать
    в entry_katka

    member_id получает ID авторизованого пользователя, именно он при нажатии Вступить в катку записывается в
    колонку members
    '''
    global ktk_item
    global member_id
    ktk_item = Katka.objects.get(pk=pk)
    member_id = request.user.id

    if request.method == 'POST':
        enter_katka(self=pk)
        return redirect('main')

    return render(request, 'katka_page/katka_page.html', {"ktk_item": ktk_item, "member_id": member_id})


def enter_katka(self):
    with connection.cursor() as cursor:
        '''
        TODO: {user.id}
        '''
        cursor.execute(f"UPDATE main_katka SET members=members||', '||{member_id} WHERE id={ktk_item.id}")


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
