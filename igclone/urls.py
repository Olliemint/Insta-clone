from django.urls import path
from . import views

app_name = 'clone'

urlpatterns =[
    path('',views.post_view,name='home'),
  
 
]