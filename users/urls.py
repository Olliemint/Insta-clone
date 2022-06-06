from django.urls import path
from . import views
from django.contrib.auth import views as authentication_views

app_name = 'user'

urlpatterns =[
    path('register/',views.register,name='register'),
    path('login/',authentication_views.LoginView.as_view(template_name='users/login.html')),
    path('logout/',authentication_views.LogoutView.as_view(template_name='users/logout.html')),


 
       
]