from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from django.contrib.auth.models import User
from django.db.models import Sum
from .forms import UserProfileForm
#imports da colega
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from blog.models import Post, Comment
from .forms import PostForm
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
#importsgio
from django.utils.text import slugify


@login_required
def profile(request, username):
    user_profile = get_object_or_404(UserProfile, user__username=username)
    post_count = Post.objects.filter(author=user_profile.user).count()
    comment_count = Comment.objects.filter(author=user_profile.user).count()
    
    user_posts = Post.objects.filter(author=user_profile.user)
    total_votes = user_posts.aggregate(
        total_votes=Sum('like_count') + Sum('silly_count') + Sum('more_count')
    )['total_votes'] or 0
    
    user_total_votes = request.user.liked_posts.aggregate(
        total_votes=Sum('like_count') + Sum('silly_count') + Sum('more_count')
    )['total_votes'] or 0
   
    context = {
        'user_profile': user_profile,
        'post_count': post_count,
        'comment_count': comment_count,
        'total_votes': total_votes,
        'user_total_votes': user_total_votes,
    }
    return render(request, 'profile.html', context)

# Bawarchi Khana code
class AddPost(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'add_post.html'
    #success_url = reverse_lazy("user_posts:manage_posts")
    form_class = PostForm
    success_message = 'Post sent. Wait for approval.'

    def form_valid(self, form):
        # gio code
        form.instance.author = self.request.user
        form.instance.status = 0
        form.instance.slug = slugify(form.instance.title)
        # Save the post and redirect to the success URL
        response = super().form_valid(form)
        return response
    
    def get_success_url(self):
        # Redirect to the manage posts page after adding a post
        return reverse_lazy("user_posts", kwargs={'username': self.request.user.username})
    
# Bawarchi Khana code
class EditPost(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'update_post.html'
    # success_url = reverse_lazy("home")

     # gio code
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(
            self.request, f'Post "{form.instance}" updated successfully'
            )
        return response
    
    def get_success_url(self):
        # Redirect to the manage posts page after adding a post
        return reverse_lazy("post_detail", kwargs={'slug': self.object.slug})
    

# Bawarchi Khana code
class DeletePost(LoginRequiredMixin, generic.DeleteView):
    
    model = Post
    template_name = 'delete_post.html'
    # success_url = reverse_lazy('home')

    # gio code
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        # response = super().delete(request, *args, **kwargs)
        messages.success(
            self.request, f'Post "{self.object}" deleted successfully'
            )

        return HttpResponseRedirect(success_url)
    
    def get_success_url(self):
        # Redirect to the manage posts page after adding a post
        return reverse_lazy("user_posts", kwargs={'username': self.request.user.username})

@login_required
def ManagePosts(request, username):
    user_posts = Post.objects.filter(approved=True, author=request.user) 
   
    context = {
        'user_posts': user_posts,
    }
    return render(request, 'manage_posts.html', context)

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