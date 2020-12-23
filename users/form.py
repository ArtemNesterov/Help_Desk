from django import forms
from users import models
from users.models import User
from django.contrib.auth.forms import UserCreationForm, UsernameField


class RegisterForm(UserCreationForm):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email")
        field_classes = {'username': UsernameField}
