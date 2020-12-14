from django.urls import path
from . import views
from django.conf.urls import include, url


urlpatterns = [
    url('', views.user_login, name='user_login'),
]