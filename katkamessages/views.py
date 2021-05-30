from django.shortcuts import render, get_object_or_404
from django.contrib.contenttypes.models import ContentType
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views import View

from .models import KatkaMessage
from .forms import KatkaMessageForm


class MessageCreateView(View):

    @staticmethod
    def post(request, *args, **kwargs):
        form = KatkaMessageForm(request.POST or None)
        ct = ContentType.objects.get(model=kwargs['content_type'])
        model = ct.model_class().objects.get(pk=kwargs['object_id'])
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.text = form.cleaned_data['text']
            new_comment.content_object = model
            new_comment.save()
            return HttpResponseRedirect(model.get_absolute_url())
        messages.add_message(request, messages.ERROR, 'Не удалось оставить комментарий')
        return HttpResponseRedirect(model.get_absolute_url())
