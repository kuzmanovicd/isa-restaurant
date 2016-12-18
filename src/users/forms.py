from django import forms
from django.core import validators

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=24)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField(validators=[validators.validate_email])
    first_name = forms.CharField(max_length=24)
    last_name = forms.CharField(max_length=30)