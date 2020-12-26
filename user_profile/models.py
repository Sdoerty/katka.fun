# from django.contrib.auth.models import User
# from django.db import models
# from signup.forms import RegForm
#
#
# class UserProfile(models.Model):
#     user = models.OneToOneField(RegForm, on_delete=models.CASCADE, primary_key=True)
#     avatar = models.ImageField()
#     first_name = models.CharField(max_length=150, required=True)
#     last_name = models.CharField(max_length=150, required=True)
#     city = models.CharField(required=True)
#     date = models.DateField(required=False, default=None)
#     inst = models.CharField(required=False)
#     vk = models.CharField(required=False)
#     fb = models.CharField(required=False)
#
#     def __unicode__(self):
#         return self.user
