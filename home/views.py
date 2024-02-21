from django.shortcuts import render
# from .models import Home

# Create your views here.

def home(request):
    return render(request, 'home/home.html')
