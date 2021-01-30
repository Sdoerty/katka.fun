from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    avatar = models.ImageField(upload_to='avatars/users/%Y/%m/%d', blank=True)
    city = models.CharField(max_length=150, blank=True, null=True)
    date_of_birth = models.DateField(max_length=150, blank=True, null=True)
    inst = models.CharField(max_length=150, blank=True, null=True)
    vk = models.CharField(max_length=150, blank=True, null=True)
    fb = models.CharField(max_length=150, blank=True, null=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


# class Activity(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     activity = models.CharField(max_length=150, blank=True, null=True)
#
#     def __str__(self):
#         return self.activity
#
#     class Meta:
#         verbose_name = 'Активность'
#         verbose_name_plural = 'Активности'
