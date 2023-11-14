from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Animes(models.Model):
    id = models.AutoField(primary_key=True)
    anime_id = models.IntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    genre = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    episodes = models.TextField(blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    members = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'animes'
    
    def __str__(self):
        return self.name


class Profile(models.Model):
    nome = models.CharField(null=True, blank=True, max_length=150)
    user = models.OneToOneField(User, related_name='profile', verbose_name='Usuário', on_delete=models.CASCADE)
    id = models.BigAutoField(primary_key=True)  # , default=80000 Valor inicial da sequência

    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfis"

    def __str__(self):
        return str(self.user.pk)
    
    @property
    def first_name(self):
        return self.user.first_name


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class Rating(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    anime = models.ForeignKey(Animes, on_delete=models.CASCADE, related_name='ratings')
    rating = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rating'
