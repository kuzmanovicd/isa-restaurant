from django import forms
from django.core import validators
from django.contrib.auth.models import User
from .models import Korisnik

class UserForm(forms.ModelForm):
    # username = forms.CharField(label='Korisnicko ime', max_length=24)
    password = forms.CharField(label='Lozinka', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Korisnik