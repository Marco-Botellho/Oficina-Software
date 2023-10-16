from django.db import models

"""
class Usuario(models.Model):
    nome = models.TextField(max_length=100)
    sobrenome = models.TextField(max_length=100)
    email = models.EmailField(unique=True)"""
"""
class TimeStampedModel(models.Model):
    created = models.DateTimeField(
        'criado em',
        auto_now_add=True,
        auto_now=False
    )
    modified = models.DateTimeField(
        'modificado em',
        auto_now_add=False,
        auto_now=True
    )

    class Meta:
        abstract = True


class Active(models.Model):
    active = models.BooleanField('ativo', default=True)

    class Meta:
        abstract = True"""