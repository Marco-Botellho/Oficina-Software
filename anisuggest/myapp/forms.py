"""
# accounts/forms.py
from django import forms
#from .models import Usuario


from accounts.models import User


class UsuarioForm(forms.ModelForm):
    first_name = forms.CharField(
        label='Nome',
        max_length=150,
    )
    last_name = forms.CharField(
        label='Sobrenome',
        max_length=150,
    )
    email = forms.EmailField(
        label='E-mail',
    )

    class Meta:
        model = Usuario
        fields = (
            'nome',
            'sobrenome',
            'email',
        )""" 