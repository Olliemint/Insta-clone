from django.shortcuts import render,redirect

from .forms import RegisterForm
from .models import Profile

# Create your views here.

def register(request):
    
    form = RegisterForm()
    
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        
        
        if form.is_valid():
            
            created_user = form.save()
            created_user.first_name = form.cleaned_data['fullname'].split(" ")[1]
            created_user.last_name = form.cleaned_data['fullname'].split(" ")[0]
            created_user.save()
            return redirect('user:login') 
            
                  
            
        
        else:
            form = RegisterForm()
    
    context = {
        'form': form,
    }
    
    
    return render(request, 'users/register.html',context)



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
