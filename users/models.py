from django.db import models
from django.contrib.auth.models import User





# Create your models here.

class Profile(models.Model):
    
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    profile_img = models.ImageField(default='raptor.jpg',upload_to='profilepics')
    id_user= models.IntegerField(default=1)
    location = models.CharField(max_length=100,blank=True)
    bio = models.TextField(max_length=200,blank=True)
    
    
    def __str__(self):
        
        return self.user.username 
    
    
   
    
    

