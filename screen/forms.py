from django import forms
from .models import *

class ScreenTypeForm(forms.ModelForm):
    class Meta:
        model = ScreenType
        fields = ['name', 'description', 'status']


class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ['name', 'description', 'location', 'latitude', 'longitude', 'status']