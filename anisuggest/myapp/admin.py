from django.contrib import admin
from .models import Animes, Profile, Rating

# Register your models here.

class AnimesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'genre', 'type','episodes', 'rating', 'members']

admin.site.register(Animes, AnimesAdmin)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'user_id']

admin.site.register(Profile, ProfileAdmin)


class RatingAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'anime_id', 'rating']

admin.site.register(Rating, RatingAdmin)
