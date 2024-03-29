from django.db import models
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.conf import settings


class KatkaMessage(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Автор сообщения', on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    text = models.TextField(verbose_name='Текст комментария')
    created_at = models.DateTimeField(editable=False)

    def __str__(self):
        return f"{self.id}"

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        super().save(*args, **kwargs)
