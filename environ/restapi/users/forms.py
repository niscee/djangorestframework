from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser
from django.contrib.auth import authenticate


#register form.
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ['email', 'username', 'password1', 'password2']


#profile update form.
class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ['email', 'username']


#login form.
class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = CustomUser
        fields = ['email','password']          