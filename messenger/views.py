from django.shortcuts import render, redirect
from django.urls import reverse
from urllib.parse import urlencode
from messenger.models import PrivateChatRoom, RoomChatMessage
from signup.models import Account
from .utils import find_or_create_private_chat
from itertools import chain
from datetime import datetime
import pytz
import json

from django.http import HttpResponse

from django.conf import settings

DEBUG = False


def private_chat_room_view(request, *args, **kwargs):
    room_id = request.GET.get("room_id")
    user = request.user
    if not user.is_authenticated:
        base_url = reverse('login')
        query_string = urlencode({'next': f"/chat/?room_id={room_id}"})
        url = f"{base_url}?{query_string}"
        return redirect(url)

    context = {}

    context['m_and_f'] = get_recent_chatroom_messages(user)

    context["BASE_URL"] = settings.BASE_URL
    if room_id:
        context["room_id"] = room_id
    context['debug'] = DEBUG
    context['debug_mode'] = settings.DEBUG
    return render(request, "messenger/messenger.html", context)


def get_recent_chatroom_messages(user):
    """
    sort in terms of most recent chats (users that you most recently had conversations with)
    """
    # 1. Find all the rooms this user is a part of
    rooms1 = PrivateChatRoom.objects.filter(user1=user)
    rooms2 = PrivateChatRoom.objects.filter(user2=user)

    # 2. merge the lists
    rooms = list(chain(rooms1, rooms2))

    # 3. find the newest msg in each room
    m_and_f = []
    for room in rooms:
        # Figure out which user is the "other user" (aka friend)
        if room.user1 == user:
            friend = room.user2
        else:
            friend = room.user1

        try:
            message = RoomChatMessage.objects.filter(room=room, user=friend).latest("timestamp")
        except RoomChatMessage.DoesNotExist:
            # create a dummy message with dummy timestamp
            today = datetime(
                year=1950,
                month=1,
                day=1,
                hour=1,
                minute=1,
                second=1,
                tzinfo=pytz.UTC
            )
            message = RoomChatMessage(
                user=friend,
                room=room,
                timestamp=today,
                content="",
            )
        m_and_f.append({
            'message': message,
            'friend': friend
        })

    return sorted(m_and_f, key=lambda x: x['message'].timestamp, reverse=True)


# Ajax call to return a private chatroom or create one if does not exist
def create_or_return_private_chat(request, *args, **kwargs):
    user1 = request.user
    payload = {}
    if user1.is_authenticated:
        if request.method == "POST":
            user2_id = request.POST.get("user2_id")
            try:
                user2 = Account.objects.get(pk=user2_id)
                chat = find_or_create_private_chat(user1, user2)
                print("Successfully got the chat")
                payload['response'] = "Successfully got the chat."
                payload['chatroom_id'] = chat.id
            except Account.DoesNotExist:
                payload['response'] = "Unable to start a chat with that user."
    else:
        payload['response'] = "You can't start a chat if you are not authenticated."
    return HttpResponse(json.dumps(payload), content_type="application/json")
