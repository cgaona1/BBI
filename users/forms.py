from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import AuthUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = AuthUser
        fields = UserCreationForm.Meta.fields

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = AuthUser
        fields = UserChangeForm.Meta.fields