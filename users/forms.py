
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'focus:outline-none','placeholder':'e.g example@gmail.com'}))
    fullname = forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'focus:outline-none','placeholder':'e.g john'}))
    
    username = forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'focus:outline-none','placeholder':'e.g john'}))
    password1 = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'focus:outline-none'}))
    
    class Meta:
        model = User
        fields = ("email","fullname","username","password1")
    
    

