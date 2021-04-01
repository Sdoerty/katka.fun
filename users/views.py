from django.shortcuts import render
from django.contrib.auth.models import User
from profile.models import Profile


def index(request):
    usu = User.objects.all()
    return render(request, 'users/users.html', {"usu": usu})


def some(request, pk):
    some_item = User.objects.get(pk=pk)
    prfl = Profile.objects.filter(pk=pk)
    return render(request, 'some/some.html', {"some_item": some_item, "prfl": prfl})
