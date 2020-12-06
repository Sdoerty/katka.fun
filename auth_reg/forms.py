from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegForm(UserCreationForm):
    email = forms.EmailField(max_length=150, label='Почта', widget=forms.EmailInput(attrs={'class': 'form-control m-b-10'}))
    first_name = forms.CharField(max_length=100, label='Имя', widget=forms.TextInput(attrs={'class': 'form-control m-b-10'}))
    last_name = forms.CharField(max_length=100, label='Фамилия',
                                widget=forms.TextInput(attrs={'class': 'form-control m-b-10'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control m-b-10'}))
    password2 = forms.CharField(label='Повторить пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    # activities = forms.ImageField(label='Интересы', required=False)
    # location = forms.CharField(label='Город', required=False)
    # born_date = forms.DateField(label='Дата рождения', required=False)
    # social_inst = forms.CharField(label='Инстаграм', required=False)
    # social_vk = forms.CharField(label='Вконтакте', required=False)
    # social_fb = forms.CharField(label='Фейсбук', required=False)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')
