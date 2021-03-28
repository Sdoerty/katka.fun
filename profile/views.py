from django.db import transaction
from .forms import ProfileEditForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Profile


def index(request):
    prfl = Profile.objects.filter(user_id=request.user.id)
    return render(request, 'profile/profile.html', {"prfl": prfl})


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
