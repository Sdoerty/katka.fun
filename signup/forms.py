from django import forms
from django.contrib.auth.models import User


class UserRegistrationForm(forms.ModelForm):
    # username = forms.CharField(max_length=150)
    # first_name = forms.CharField(max_length=150)
    # last_name = forms.CharField(max_length=150)
    password1 = forms.CharField(max_length=150)
    password2 = forms.CharField(max_length=150)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')
