from django import forms
from .models import PredictionInput

class PredictionForm(forms.ModelForm):
    class Meta:
        model = PredictionInput
        fields = '__all__'