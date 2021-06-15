from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model=CustomUser
        # fields = UserCreationForm.Meta.fields + ('age',)
        fields = ('username', 'email', 'age',) # new


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model=CustomUser
        # fields = UserChangeForm.Meta.fields
        fields = ('username', 'email', 'age',) # new


