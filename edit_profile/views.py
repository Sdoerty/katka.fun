from django.contrib.auth.forms import UserChangeForm
from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from .forms import EditProfileForm

from django.contrib.auth.decorators import login_required


@login_required
def edit_profile(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
    else:
        form = EditProfileForm(instance=request.user)
    args = {'form': form}
    return render(request, 'edit_profile/edit_profile.html', args)

# class EditProfile(generic.UpdateView):
#     form_class = UserChangeForm
#     template_name = 'edit_profile/edit_profile.html'
#     success_url = reverse_lazy('user_profile')
#
#     # Получаем заполненные данные авторизованного пользователя в полях для редактирования
#     def get_object(self, queryset=None):
#         return self.request.user
