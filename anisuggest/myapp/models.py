from django.db import models

class Usuario(models.Model):
    nome = models.TextField(max_length=100)
    sobrenome = models.TextField(max_length=100)
    email = models.EmailField(unique=True)

