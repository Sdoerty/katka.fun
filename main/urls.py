from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    url(r'^table/$', views.index, name='main'),
    url(r'^katka_page/$', views.katka_page, name='katka_page'),
    url(r'^create_katka/$', views.create_katka, name='create_katka'),
]