from django import forms
from django.views.generic import DetailView

from .models import Profile


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('avatar', 'city', 'date_of_birth', 'inst', 'vk', 'fb', 'act')

