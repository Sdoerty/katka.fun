from django.urls import path
from . import views
from django.conf.urls import include, url


urlpatterns = [
    url('', views.edit_profile, name='edit_profile'),
]