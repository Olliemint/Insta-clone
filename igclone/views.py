from django.shortcuts import render

# Create your views here.

def post_view(request):
    
    return render(request,'clone/home.html')
