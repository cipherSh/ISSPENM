from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user']