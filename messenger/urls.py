from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url('', views.private_chat_room_view, name='messenger'),
]