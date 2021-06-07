from django.contrib import admin
from .models import PrivateChatRoom, RoomChatMessage

admin.site.register(PrivateChatRoom)
admin.site.register(RoomChatMessage)
