from django.contrib.auth.forms import UserChangeForm
from django.views import generic
from django.urls import reverse_lazy


class EditProfile(generic.UpdateView):
    form_class = UserChangeForm
    template_name = 'edit_profile/edit_profile.html'
    success_url = reverse_lazy('user_profile')

    # Получаем заполненные данные авторизованного пользователя в полях для редактирования
    def get_object(self, queryset=None):
        return self.request.user
