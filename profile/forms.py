from django import forms
from .models import Profile


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('avatar', 'city', 'date_of_birth', 'inst', 'vk', 'fb', 'act')

