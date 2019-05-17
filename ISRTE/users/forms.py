from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'last_name', 'first_name')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('role_id', 'trust_level_id', 'birth_date')


class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
