from django.contrib.auth.forms import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class SignupForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','username','email','is_writer','password1','password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['bio','avatar']

class  LoginForm(forms.Form):
    user_name=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput,max_length=20)