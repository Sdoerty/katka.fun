from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    email = forms.EmailField(max_length=150, label='Почта',
                             widget=forms.EmailInput(attrs={'class': 'form-control m-b-10'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control m-b-10'}))


