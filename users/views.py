from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from .models import Profile

# Create your views here.

def Login_user(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
    
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('clone:home')
        
        else:
            
            messages.warning(request,"Invalid username or password")
            
            return redirect('user:login')
    
    
    
    
    
    return render(request,'users/login.html')
    
    
    
    
         
    

def Register_user(request,min_length=8):
    
    if request.method == 'POST':
        email = request.POST['email']
        fullname = request.POST['fullname']
        username = request.POST['username']
        password = request.POST['password']
        
        first_name, last_name = fullname.split()
        
        
        if len(password) > min_length:
            
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email already exists')
                return redirect('user:register')
            
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username already exists')
                return redirect('user:register')
            
            else:
                hashed_password = make_password('password')
                user = User.objects.create(username=username,first_name=first_name,last_name =last_name,email=email,password=hashed_password)
                user.save()
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model,id_user=user_model.id)
                return redirect('user:login')

                
        else:
            messages.info(request,'Password length mismatch')  
            return redirect('user:register')
              
    
    return render(request, 'users/register.html')



def profile(request):
    
    
    return render(request, 'users/profile.html')


def edit_profile(request):
    if request.method == 'POST':
        image = request.POST.get('upload')
        bio = request.POST.get('bio')
        contact = request.POST.get('contact')
        gender = request.POST.get('gender')
        user = request.user
        
        profile = Profile.objects.create(user=user, image=image)
        profile.save()
    
    
    return render(request, 'users/editprofile.html')
