from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import UserProfile, UsersPostRequest
from .forms import UsersPostForm 

# Create your views here.

def profile(request, username):
     user_profile = get_object_or_404(UserProfile, user__username=username)
     user_posts = UsersPostRequest.objects.filter(approved=True)
     # additional information such as liked posts, commented posts, etc., here
     context = {
         'user_profile': user_profile,
         'userspost_form': UsersPostForm(),
         'user_posts': user_posts,
     }
     return render(request, 'profile.html', context)

def user_posts(request, username):
    if request.method == "POST":
        userspost_form = UsersPostForm(data=request.POST)
        if userspost_form.is_valid():
            users_post = userspost_form.save(commit=False)
            users_post.approved = False
            userspost_form.save()
            # messages.add_message(request, messages.SUCCESS, "Post received! We'll approve it with 2 days.")
            messages.success(request, "Post received! We'll approve it within 2 days.")
            return redirect('profile', username=username)
        else:
            messages.error(request, "Post submission failed. Please check your form.")
    else:
        userspost_form = UsersPostForm()


    user_profile = get_object_or_404(UserProfile, user__username=username)
    context = {
        "user_profile": user_profile,
        "userspost_form": userspost_form,
    }

    return render(request, 'profile.html',
        {
            "userspost_form": userspost_form
        },
    
    )