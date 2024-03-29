from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from multiselectfield import MultiSelectField
from main.activities import ACTIVITY
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    avatar = models.ImageField(upload_to='avatars/users/%Y/%m/%d', blank=True)
    city = models.CharField(max_length=150, blank=True, null=True)
    date_of_birth = models.DateField(max_length=150, blank=True, null=True)
    inst = models.CharField(max_length=150, blank=True, null=True)
    vk = models.CharField(max_length=150, blank=True, null=True)
    fb = models.CharField(max_length=150, blank=True, null=True)
    act = MultiSelectField(choices=ACTIVITY, max_choices=20, max_length=1500, blank=True, null=True)

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
