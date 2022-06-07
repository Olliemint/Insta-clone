from django.urls import path
from . import views

app_name = 'clone'

urlpatterns =[
    path('',views.post_view,name='home'),
    path('posts/add',views.add_post,name='add_post'),
    path('comment/',views.comment,name='comment'),
    
    

  
 
]