from django.urls import path
from django.conf.urls import url


from .views import MessageCreateView

urlpatterns = [
    path('create/<str:content_type>/<int:object_id>/', MessageCreateView.as_view(), name='message-create')
]

app_name = 'katkamessages'
