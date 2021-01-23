from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.urls import path, include

from profile import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('login.urls')),
    path('signup/', include('signup.urls')),
    path('main/', include('main.urls')),
    path('profile/', include('profile.urls')),
    path('users/', include('users.urls')),
    path('login/', views.index, name='login'),
    path('signup/', views.index, name='signup'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
