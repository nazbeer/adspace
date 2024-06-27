from django.forms import ModelForm,forms
from .models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.admin import UserAdmin
from django import forms

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email','username','first_name','last_name','phone_number','role')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email','first_name','last_name','phone_number','role')


