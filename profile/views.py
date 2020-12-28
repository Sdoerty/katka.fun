from django.shortcuts import render, redirect
from .forms import EditProfileForm
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'profile/profile.html')


@login_required
def edit_profile(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditProfileForm(instance=request.user)
    args = {'form': form}
    return render(request, 'edit_profile/edit_profile.html', args)
