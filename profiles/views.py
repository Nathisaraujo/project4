from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.text import slugify
from django.db.models import Sum, Q
from django.views import generic, View
from .forms import UserProfileForm, PostForm
from blog.models import Post, Comment
from .models import UserProfile

# Profile view - displays the user profile information
@login_required
def profile(request, username):
    user_profile = get_object_or_404(UserProfile, user__username=username)
    post_count = Post.objects.filter(author=user_profile.user).count()
    comment_count = Comment.objects.filter(author=user_profile.user).count()
    user_posts = Post.objects.filter(author=user_profile.user)
    
    # Displays the counts for the user statistics
    post_total_votes = user_posts.aggregate(
        post_total_votes=Sum('like_count') + Sum('silly_count') + Sum('more_count')
    )['post_total_votes'] or 0

    user_total_votes = Post.objects.filter(
        Q(like_count__gt=0, liked=user_profile.user) |
        Q(silly_count__gt=0, sillied=user_profile.user) |
        Q(more_count__gt=0, more=user_profile.user)
    ).distinct().count()

    context = {
        'user_profile': user_profile,
        'post_count': post_count,
        'comment_count': comment_count,
        'post_total_votes': post_total_votes,
        'user_total_votes': user_total_votes,
    }
    return render(request, 'profile.html', context)

# Add post view from Bawarchi Khana's code with modifications
class AddPost(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'add_post.html'
    form_class = PostForm
    success_message = 'Post sent. Wait for approval.'

    def form_valid(self, form):
        # Just Blog's piece of code
        form.instance.author = self.request.user
        form.instance.status = 0
        form.instance.slug = slugify(form.instance.title)
        response = super().form_valid(form)
        return response
    
    def get_success_url(self):
        return reverse_lazy("user_posts", kwargs={'username': self.request.user.username})
    
# Edit post view from Bawarchi Khana's code with modifications
class EditPost(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'update_post.html'

    # function from Just Blog's code
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(
            self.request, f'Post "{form.instance}" updated successfully'
            )
        return response
    
    def get_success_url(self):
        return reverse_lazy("post_detail", kwargs={'slug': self.object.slug})
    

# Delete post view from Bawarchi Khana's code with modifications
class DeletePost(LoginRequiredMixin, generic.DeleteView):
    
    model = Post
    template_name = 'delete_post.html'

    # function from Just Blog's code
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        messages.success(
            self.request, f'Post "{self.object}" deleted successfully'
            )

        return HttpResponseRedirect(success_url)
    
    def get_success_url(self):
        return reverse_lazy("user_posts", kwargs={'username': self.request.user.username})

# Manage post view
@login_required
def ManagePosts(request, username):
    user_posts = Post.objects.filter(approved=True, author=request.user) 
   
    context = {
        'user_posts': user_posts,
    }
    return render(request, 'manage_posts.html', context)

# User Activity view
@login_required
def user_activity(request, username):
    user = User.objects.get(username=username)
    liked_posts = Post.objects.filter(liked=request.user)
    silly_posts = Post.objects.filter(sillied=request.user)
    more_posts = Post.objects.filter(more=request.user)
    commented_posts = Post.objects.filter(comments__author=user)
   
    context = {
        'liked_posts': liked_posts,
        'silly_posts': silly_posts,
        'more_posts': more_posts,
        'commented_posts': commented_posts,

    }
    return render(request, 'user_activity.html', context)

# Edit Profile view
@login_required
def edit_profile(request, username):
     user_profile = request.user.userprofile

     if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile', username=request.user.username)
     else:
        form = UserProfileForm(instance=user_profile)

     return render(request, 'edit_profile.html', {'form': form})