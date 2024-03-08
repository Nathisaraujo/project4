from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile


@login_required
def profile(request, username):
    user_profile = get_object_or_404(UserProfile, user__username=username) 
   
    context = {
        'user_profile': user_profile,
    }
    return render(request, 'profile.html', context)
