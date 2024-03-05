from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from .forms import UsersPostForm

# Create your views here.

def profile(request, username):
     user_profile = get_object_or_404(UserProfile, user__username=username)
     # additional information such as liked posts, commented posts, etc., here
     context = {
         'user_profile': user_profile,
         'userspost_form': UsersPostForm(),
     }
     return render(request, 'profile.html', context)

def user_posts(request, username):
    if request.method == "POST":
        userspost_form = UsersPostForm(data=request.POST)
        if userspost_form.is_valid():
            userspost_form.save()
            messages.add_message(request, messages.SUCCESS, "Post received! We'll approve it with 2 days.")
            
    userspost_form = UsersPostForm()

    return render(request, 'profile.html',
        {
            "userspost_form": userspost_form
        },
    
    )
