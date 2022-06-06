from django.shortcuts import render
from .models import Feed

# Create your views here.

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
        
        post = Feed(image=image, caption=caption)
        post.save()
        
        
        
    
    
    return render(request,'clone/home.html')
    
    
    
    
