from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    # url('', views.index, name='profile'),
    url(r'^edit_profile/$', views.edit, name='edit_profile'),
]