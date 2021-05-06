from django.db import transaction
from .forms import ProfileEditForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Profile
from signup.models import Account
from friendship.models import Friend, Follow, Block


def index(request):
    prfl = Profile.objects.filter(user_id=request.user.id)

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

    return render(request, 'profile/profile.html',
                  {"prfl": prfl, "count_of_followers": count_of_followers, "count_of_followings": count_of_followings})


@login_required
@transaction.atomic
def edit(request):
    if request.method == 'POST':
        profile_form = ProfileEditForm(request.POST, request.FILES, instance=request.user.profile)

        if profile_form.is_valid():
            profile_form.save()
    else:
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request,
                  'edit_profile/edit_profile.html',
                  {'profile_form': profile_form})
