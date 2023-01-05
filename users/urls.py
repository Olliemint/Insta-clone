from django.urls import path
from . import views
from django.contrib.auth import views as authentication_views

app_name = 'user'

urlpatterns =[
    path('register/',views.Register_user,name='register'),
    path('login/',views.Login_user,name='login'),
    path('logout/',authentication_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('profile/',views.profile,name='profile'),
    path('editprofile/',views.edit_profile,name='edit'),
    


 
       
]