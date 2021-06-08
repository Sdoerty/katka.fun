from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^table/$', views.index, name='main'),
    url(r'^katka/(?P<pk>\d+)/$', views.katka_page, name='katka'),
    url(r'^create_katka/$', views.create_katka, name='create_katka'),
]