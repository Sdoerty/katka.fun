from django.db import models
from django.urls import reverse
from profile.models import Profile


class Users(Profile):
    def get_absolute_url(self):
        return reverse('users', kwargs={'pk': self.pk})
