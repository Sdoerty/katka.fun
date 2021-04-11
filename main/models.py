from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from multiselectfield import MultiSelectField
from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from profile.models import Profile
from .activities import ACTIVITY
from django.conf import settings



class Katka(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    city = models.CharField(max_length=150)
    date = models.DateField(max_length=150)
    time = models.TimeField(max_length=150)
    descr = models.CharField(max_length=350)
    katka_act = MultiSelectField(choices=ACTIVITY)
    members = models.ManyToManyField(Profile, related_name="profile_set")

    def get_absolute_url(self):
        return reverse('katka', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Катка'
        verbose_name_plural = 'Все события Катка'
        ordering = ['-id']
