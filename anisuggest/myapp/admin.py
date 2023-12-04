from django.contrib import admin
from .models import Animes, Profile, Rating

# Register your models here.

class AnimesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'genre', 'type','episodes', 'rating', 'anime_id']

admin.site.register(Animes, AnimesAdmin)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'user_id', 'user']

admin.site.register(Profile, ProfileAdmin)


class RatingAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'anime_id', 'rating', 'id']

admin.site.register(Rating, RatingAdmin)
