from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.views.generic import RedirectView

from user_profile import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth_reg/', include('allauth.urls')),
    path('auth_reg/', include('auth_reg.urls')),
    path('mainpage/', include('mainpage.urls')),
    path('mainpage/', views.index, name='mainpage'),
    path('user_profile/', include('user_profile.urls')),
    path('user_profile/', views.index, name='user_profile'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
