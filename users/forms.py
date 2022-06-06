
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'focus:outline-none','placeholder':'Email'}))
    fullname = forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'focus:outline-none','placeholder':'Full Name'}))
    
    username = forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'focus:outline-none','placeholder':'Username'}))
    password1 = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'focus:outline-none','placeholder':'Password'}))
    password2 = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'focus:outline-none','placeholder':'Confirm Password'}))

    
    class Meta:
        model = User
        fields = ("email","fullname","username","password1","password2")
    
    

