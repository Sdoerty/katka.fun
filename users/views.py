from django.shortcuts import render
from django.contrib.auth.models import User


def index(request):
    usu = User.objects.all()
    return render(request, 'users/users.html', {"usu": usu})

def some(request, pk):
    some_item = User.objects.get(pk=pk)
    return render(request, 'users/some.html', {"some_item": some_item})