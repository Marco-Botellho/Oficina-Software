from django.contrib import admin
from .models import Animes

# Register your models here.

class AnimesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'genre', 'type','episodes', 'rating', 'members']

admin.site.register(Animes, AnimesAdmin)
