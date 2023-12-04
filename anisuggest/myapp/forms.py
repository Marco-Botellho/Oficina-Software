from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import Rating

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating']
        widgets = {
            'rating': forms.NumberInput(attrs={'type': 'number', 'min': '1', 'max': '10'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['rating'].validators.append(MinValueValidator(1))
        self.fields['rating'].validators.append(MaxValueValidator(10))