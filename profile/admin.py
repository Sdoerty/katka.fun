from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'avatar', 'city', 'date_of_birth', 'inst', 'vk', 'fb', 'act')
