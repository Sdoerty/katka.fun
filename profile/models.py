from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
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


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    avatar = models.ImageField(upload_to='avatars/users/%Y/%m/%d', blank=True)
    city = models.CharField(max_length=150, blank=True, null=True)
    date_of_birth = models.DateField(max_length=150, blank=True, null=True)
    inst = models.CharField(max_length=150, blank=True, null=True)
    vk = models.CharField(max_length=150, blank=True, null=True)
    fb = models.CharField(max_length=150, blank=True, null=True)
    act = MultiSelectField(choices=ACTIVITY, blank=True, null=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return str(self.user.first_name)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
