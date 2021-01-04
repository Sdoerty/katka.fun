from django.contrib import admin
from .models import Katka


@admin.register(Katka)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'city', 'date', 'time', 'k_descriptions')
