from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^all/$', views.index, name='users'),
    url(r'^some/(?P<pk>\d+)/$', views.some, name='some'),

]
