from django.contrib import admin
from .models import Profile
# from .models import Activity


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'avatar', 'city', 'date_of_birth', 'inst', 'vk', 'fb')

#
# @admin.register(Activity)
# class ActivityAdmin(admin.ModelAdmin):
#     list_display = ('user', 'activity')
