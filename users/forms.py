
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms


class NewUserForm(UserCreationForm):
    
    username = forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'focus:outline-none','placeholder':'e.g john'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'focus:outline-none','placeholder':'e.g example@gmail.com'}))
    password1 = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'focus:outline-none'}))
    password2 = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'focus:outline-none'}))
    
    class Meta:
        model = User
        fields = ("username","email","password1","password2")
    
    

