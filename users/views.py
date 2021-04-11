from django.shortcuts import render
from django.contrib.auth.models import User
from profile.models import Profile
from django.conf import settings
from signup.models import Account

# Account - это новая модель вместо стандартной USER -------------------------------------

def index(request):
    usu = Account.objects.all()
    return render(request, 'users/users.html', {"usu": usu})


def some(request, pk):
    some_item = Account.objects.get(pk=pk)
    prfl = Profile.objects.filter(pk=pk)
    return render(request, 'some/some.html', {"some_item": some_item, "prfl": prfl})
