from django import forms
from .models import ScreenType

class ScreenTypeForm(forms.ModelForm):
    class Meta:
        model = ScreenType
        fields = ['name', 'description', 'status']
