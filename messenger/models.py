from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils import timezone


class PrivateChatRoom(models.Model):
    user1 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user1")
    user2 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user2")

    # Users who are currently connected to the socket (Used to keep track of unread messages)
    connected_users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="connected_users")

    @property
    def group_name(self):
        return f"PrivateChatRoom-{self.id}"


class RoomChatMessageManager(models.Manager):
    def by_room(self, room):
        qs = RoomChatMessage.objects.filter(room=room).order_by("-timestamp")
        return qs


class RoomChatMessage(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey(PrivateChatRoom, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField(unique=False, blank=False, )

    objects = RoomChatMessageManager()

    def __str__(self):
        return self.content
