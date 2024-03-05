from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import UserProfile  

# Create your views here.

def profile(request, username):
     user_profile = get_object_or_404(UserProfile, user__username=username)
     # additional information such as liked posts, commented posts, etc., here
     context = {
         'user_profile': user_profile,
     }
     return render(request, 'profile.html', context)
