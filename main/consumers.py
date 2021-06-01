import json
from django.contrib.contenttypes.models import ContentType
from channels.db import database_sync_to_async
from asgiref.sync import async_to_sync
from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from katkamessages.models import KatkaMessage
from .models import Katka
from profile.models import Profile


class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.katka_pk = self.scope['url_route']['kwargs']['pk']
        self.katka_group_name = 'katka_%s' % self.katka_pk

        # Join room group
        await self.channel_layer.group_add(
            self.katka_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.katka_group_name,
            self.channel_name
        )


    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        comment = text_data_json['text']
        new_comment = await self.create_new_comment(comment)
        data = {'author_f': new_comment.author.first_name,
                'author_l': new_comment.author.last_name,
                'created_at': new_comment.created_at.strftime('%d-%m-%Y %H:%m'),
                'text': new_comment.text}
        # Send message to room group
        await self.channel_layer.group_send(
            self.katka_group_name,
            {
                'type': 'new_comment',
                'message': data
            }
        )

    # Receive message from room group
    async def new_comment(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))

    @database_sync_to_async
    def create_new_comment(self, text):
        ct = ContentType.objects.get_for_model(Katka)
        new_comment = KatkaMessage.objects.create(
            author=self.scope['user'],
            text=text,
            content_type=ct,
            object_id=int(self.katka_pk)
        )
        return new_comment
