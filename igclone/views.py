from django.shortcuts import render, redirect
from .models import Feed
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def post_view(request):
    
    posts = Feed.objects.all()
    context = {
        'posts': posts
    }
    
    return render(request,'clone/home.html',context)



def add_post(request):
    if request.method == 'POST':
        
        image = request.FILES.get('upload')
        
        caption = request.POST.get('caption')
        print(image, caption)
        
        post = Feed.objects.create(image=image, caption=caption)
        return redirect('clone:home')        
        
        
    
    
    return render(request,'clone/home.html')
    
    
    
    
