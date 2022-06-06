from django.db import models

# Create your models here.

class Feed(models.Model):
    image = models.ImageField(null=True, blank= True, upload_to= 'images')
    caption = models.CharField(max_length=100, blank=False,null=False)
    def __str__(self):
        return self.caption 
    
