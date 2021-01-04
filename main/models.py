from django.db import models


class Katka(models.Model):
    id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=150)
    date = models.DateField(max_length=150)
    time = models.TimeField(max_length=150)
    k_descriptions = models.CharField(max_length=350)