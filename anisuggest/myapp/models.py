from django.db import models

class Animes(models.Model):
    anime_id = models.IntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    genre = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    episodes = models.IntegerField(blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    members = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'animes'


class Rating(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    anime_id = models.IntegerField(blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rating'
