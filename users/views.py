from django.shortcuts import render
from django.contrib.auth.models import User
from profile.models import Profile
from django.conf import settings
from signup.models import Account
from django.contrib.auth.decorators import login_required
from django.conf import settings
from friendship.models import Friend, Follow, Block
from friendship.models import FriendshipRequest


# Account - это новая модель вместо стандартной USER -------------------------------------

def index(request):
    usu = Account.objects.all()
    return render(request, 'users/users.html', {"usu": usu})


def some(request, pk):
    some_item = Account.objects.get(pk=pk)
    prfl = Profile.objects.filter(pk=pk)

    if request.method == 'POST' and 'send_request' in request.POST:
        other_user = Account.objects.get(pk=pk)
        Friend.objects.add_friend(request.user, other_user, message='Hi! I would like to add you')
    elif request.method == 'POST' and 'accept_request' in request.POST:
        friend_request = FriendshipRequest.objects.get(to_user=pk)
        friend_request.accept()

    return render(request, 'some/some.html', {"some_item": some_item, "prfl": prfl})
