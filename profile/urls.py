from django.conf.urls import url
from django.urls import path
from . import views
from main.views import katka_page


urlpatterns = [
    url(r'^user/$', views.index, name='profile'),
    url(r'^edit_profile/$', views.edit, name='edit_profile'),
    url(r'^katka/(?P<pk>\d+)/$', katka_page, name='katka_page'),

]