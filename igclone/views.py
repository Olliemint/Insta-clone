

from django.http import HttpResponse
from django.shortcuts import render, redirect,get_object_or_404
from .models import Feed,Comment
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def post_view(request):
    
    
   
    
    posts = Feed.objects.order_by('-created').all()
    
    
    
    if request.method == 'POST':
        comment = request.POST.get('comment')
        user = request.user
        feed_id = request.POST.get('myid')
        feed = Feed.objects.get(id=feed_id)
        
        new_comment = Comment.objects.create(user=user,comment=comment,feed_id=feed_id)
        feed.comments.add(new_comment)
        feed.save()
        
   
       
   
    context = {
        'posts': posts,
        
       
    }
    
    return render(request,'clone/home.html',context)



def add_post(request):
    if request.method == 'POST':
        
        image = request.FILES.get('upload')
        
        caption = request.POST.get('caption')
        author = request.user
        print(image, caption)
        
        post = Feed.objects.create(image=image, caption=caption,author=author)
        return redirect('clone:home')        
        
        
    
    
    return render(request,'clone/home.html')



def view_comments(request,pk):
    
    feed = Feed.objects.get(id=pk)
    comments = Comment.objects.get(feed_id=pk)
    
    context = {
        'feed': feed,
        'comments': comments
    }
    
    
    
    return render(request,'clone/comments.html',context)





def comment(request):
    if request.method == 'POST':
        feed_id = request.POST.get('my')
    

        post = Feed.objects.get(id=feed_id)
        post.likes.add(request.user)
        
    
    
    
    return redirect("clone:home")




    
    
    
    
    

      
    
    
    
