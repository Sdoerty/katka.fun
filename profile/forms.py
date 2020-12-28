from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User


class EditProfileForm(UserChangeForm):
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    city = forms.CharField(max_length=150)
    date_of_birth = forms.DateField()
    inst = forms.CharField(max_length=150)
    vk = forms.CharField(max_length=150)
    fb = forms.CharField(max_length=150)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'city', 'date_of_birth', 'inst', 'vk', 'fb')
