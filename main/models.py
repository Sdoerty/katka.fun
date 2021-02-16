from django.db import models
from django.urls import reverse
from multiselectfield import MultiSelectField

ACTIVITY = (
    ('1', 'basketball'),
    ('2', 'bicycle'),
    ('3', 'bowling'),
    ('4', 'dancing'),
    ('5', 'football'),
    ('6', 'horse-riding'),
    ('7', 'lifting'),
    ('8', 'motocross'),
    ('9', 'ping-pong'),
    ('10', 'pullups'),
    ('11', 'rolls'),
    ('12', 'run'),
    ('13', 'skate'),
    ('14', 'skiing'),
    ('15', 'snowboard'),
    ('16', 'tennis'),
    ('17', 'trekking'),
    ('18', 'volleyball'),
    ('19', 'walking'),
    ('20', 'yoga'),
)


class Katka(models.Model):
    id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=150)
    date = models.DateField(max_length=150)
    time = models.TimeField(max_length=150)
    descr = models.CharField(max_length=350)
    katka_act = MultiSelectField(choices=ACTIVITY)

    def get_absolute_url(self):
        return reverse('katka', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Катка'
        verbose_name_plural = 'Все события Катка'

