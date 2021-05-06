from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from profile.models import Profile
from django.conf import settings
from signup.models import Account
from django.contrib.auth.decorators import login_required
from django.conf import settings
from friendship.models import Friend, Follow, Block
from friendship.models import FriendshipRequest
from django.http import HttpResponseRedirect


# Account - это новая модель вместо стандартной USER -------------------------------------

def index(request):
    usu = Account.objects.all()
    my_followers = Follow.objects.followers(request.user)
    my_following = Follow.objects.following(request.user)
    list_followers = []
    list_following = []

    for a in my_followers:
        list_followers.append(a)

    for b in my_following:
        list_following.append(b)

    count_of_followers = len(list_followers)
    count_of_followings = len(list_following)

    return render(request, 'users/users.html', {"usu": usu, "my_followers": my_followers,
                                                "my_following": my_following, "count_of_followers": count_of_followers,
                                                "count_of_followings": count_of_followings})


def some(request, pk):
    '''
    status - 0 : не подписан
    status - 1 : подписан
    '''
    some_item = Account.objects.get(pk=pk)
    prfl = Profile.objects.filter(pk=pk)
    follow_all = Follow.objects.all()
    my_followers = Follow.objects.followers(request.user)
    my_following = Follow.objects.following(request.user)
    status = 0

    if some_item in my_following:
        status = 1

    if request.method == 'POST':
        Follow.objects.add_follower(request.user, some_item)
        return HttpResponseRedirect('#')

    his_followers = Follow.objects.followers(some_item)
    his_following = Follow.objects.following(some_item)
    list_followers = []
    list_following = []

    for a in his_followers:
        list_followers.append(a)

    for b in his_following:
        list_following.append(b)

    count_of_followers = len(list_followers)
    count_of_followings = len(list_following)

    return render(request, 'some/some.html',
                  {"some_item": some_item, "prfl": prfl, "follow_all": follow_all, "his_followers": his_followers,
                   "his_following": his_following, "status": status, "count_of_followers": count_of_followers,
                   "count_of_followings": count_of_followings})
