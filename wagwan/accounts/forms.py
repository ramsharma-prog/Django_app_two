from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from . import models

# ACCOUNTS FORMS


class UserSignupForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email')


class ImageUpdateForum(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ('image',)
