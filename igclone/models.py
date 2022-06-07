from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Feed(models.Model):
    image=models.ImageField(null=True)
    caption=models.CharField(max_length=150, null=False)
    author =models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True,null=True)
    
   
    likes = models.ManyToManyField(
        User, related_name='like', blank=True)
    
    def __str__(self):
        return self.caption
    
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    comment = models.CharField(max_length=255, blank=False, null=False)
    feed = models.ForeignKey(
       Feed , blank=False, on_delete=models.CASCADE, null=False)
    created = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.comment



# class Feed(models.Model):
#     image = models.ImageField(null=True, blank= True, upload_to= 'images')
#     caption = models.CharField(max_length=100, blank=False,null=False)
#     created = models.DateTimeField(auto_now_add=True, null=True)    
    
    
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # created = models.DateTimeField(auto_now_add=True,null=True)
    # def __str__(self):
    #     return self.caption 
    
    
# class Comment(models.Model):
#     comment = models.TextField()
#     feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     created = models.DateTimeField(auto_now_add=True, null=True)    
    
