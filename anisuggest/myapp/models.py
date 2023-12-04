from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Avg


class Animes(models.Model):
    id = models.AutoField(primary_key=True) # essa é a chave estrangeira em rating
    anime_id = models.IntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    genre = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    episodes = models.TextField(blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    members = models.IntegerField(blank=True, null=True)

    def update_average_rating(self):
        # Calcula a média das avaliações para este anime
        average_rating = Rating.objects.filter(anime=self).aggregate(Avg('rating'))['rating__avg']

        # Atualiza o campo 'rating' do anime com a média calculada
        if average_rating is not None:
            self.rating = average_rating
            self.save()

    class Meta:
        managed = False
        db_table = 'animes'
    
    def __str__(self):
        return self.name


class Profile(models.Model):
    nome = models.CharField(null=True, blank=True, max_length=150)
    user = models.OneToOneField(User, related_name='profile', verbose_name='Usuário', on_delete=models.CASCADE)
    id = models.BigAutoField(primary_key=True)  # , default=80000 Valor inicial da sequência  # essa é a chave estrangeira em rating

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
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])

    class Meta:
        managed = False
        db_table = 'rating'


@receiver(post_save, sender=Rating)
def update_anime_rating(sender, instance, **kwargs):
    anime = instance.anime
    anime.update_average_rating()