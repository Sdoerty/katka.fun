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
    path('login/', views.index, name='login'),
    path('signup/', views.index, name='signup'),
    path('main/', views.index, name='main'),
    path('profile/', views.index, name='profile'),
    path('profile/edit_profile/', views.edit_profile, name='edit_profile'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
