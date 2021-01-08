from django.db import models
from django.urls import reverse


class Katka(models.Model):
    id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=150)
    date = models.DateField(max_length=150)
    time = models.TimeField(max_length=150)
    descr = models.CharField(max_length=350)

    def get_absolute_url(self):
        return reverse('katka', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Катка'
        verbose_name_plural = 'Все события Катка'

