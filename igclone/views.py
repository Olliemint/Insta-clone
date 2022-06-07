from calendar import c
from django.shortcuts import render, redirect
from .models import Feed,Comment
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def post_view(request):
    
    
    if request.method == 'POST':
        comment = request.POST.get('comment')
        user = request.user
        
        new_comment = Comment.objects.create(user=user,comment=comment)
        new_comment.save()
    
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
    
    
    
    
