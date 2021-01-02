from django.db import transaction
from .forms import ProfileEditForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def index(request):
    return render(request, 'profile/profile.html')


@login_required
@transaction.atomic
def edit(request):
    if request.method == 'POST':
        profile_form = ProfileEditForm(request.POST, instance=request.user.profile)

        if profile_form.is_valid():
            profile_form.save()
    else:
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request,
                  'edit_profile/edit_profile.html',
                  {'profile_form': profile_form})
