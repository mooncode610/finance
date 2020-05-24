from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(help_text=password_validation.password_validators_help_text_html(),
                                label='Password')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields =('username', 'first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ('profile_pic', 'birth_date')
