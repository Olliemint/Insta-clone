from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='raptor.jpg',upload_to='profilepics')
    
    def __str__(self):
        return self.user.username 
    
    
    def save_profile(self):
        self.user
        
    def save_user(self):
        self.save()   

    def delete_profile(self):
        self.delete()
    
    

