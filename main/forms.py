from django import forms
from django.contrib.auth.models import User
from .models import Katka


class KatkaForm(forms.ModelForm):
    class Meta:
        model = Katka
        fields = ('id', 'city', 'date', 'time', 'descr', 'katka_act', 'author',)


class KatkaEntryForm(forms.ModelForm):
    class Meta:
        model = Katka
        fields = ('members',)
