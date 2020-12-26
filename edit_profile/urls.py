from django.urls import path
from .views import EditProfile
from django.conf.urls import include, url


urlpatterns = [
    url('', EditProfile.as_view(), name='edit_profile'),
]