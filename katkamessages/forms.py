from django import forms

from .models import KatkaMessage


class KatkaMessageForm(forms.ModelForm):

    class Meta:
        model = KatkaMessage
        fields = ['text']
