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
    """
    Renders the user profile page with user-specific information.

    Retrieves the user profile associated with the provided username
    and renders the user profile page with user statistics.

    **Context**
    ``user_profile``
        The UserProfile instance associated with the requested username.
    ``post_count``
        The count of posts authored by the user.
    ``comment_count``
        The count of comments authored by the user.
    ``post_total_votes``
        The total number of votes received on user's posts.
    ``user_total_votes``
        The total number of posts on which the user has voted.

    **Template**
    :template:`profile.html`
    """
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
    """
    View for adding a new post.

    Allows authenticated users to add a new post. SuccessMessageMixin
    is used to display success messages after successfully adding a post.

    **Context**
    ``form``
        The PostForm instance.

    **Template**
    :template:`add_post.html`
    """
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
        return reverse_lazy("user_posts",
                            kwargs={'username': self.request.user.username})

# Edit post view from Bawarchi Khana's code with modifications


class EditPost(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    """
    View for editing a post.

    Allows authenticated users to edit their own posts. SuccessMessageMixin
    is used to display success messages after successfully updating a post.

    **Context**
    ``form``
        The PostForm instance.

    **Template**
    :template:`update_post.html`
    """
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
    """
    View for deleting a post.

    Allows authenticated users to delete their own posts.

    **Template**
    :template:`delete_post.html`
    """
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
        return reverse_lazy("user_posts",
                            kwargs={'username': self.request.user.username})

# Manage post view


@login_required
def ManagePosts(request, username):
    """
    View for managing user posts.

    Displays a list of posts authored by the authenticated user.

    **Context**
    ``user_posts``
        A queryset of posts authored by the authenticated user.

    **Template**
    :template:`manage_posts.html`
    """
    user_posts = Post.objects.filter(approved=True, author=request.user)

    context = {
        'user_posts': user_posts,
    }
    return render(request, 'manage_posts.html', context)

# User Activity view


@login_required
def user_activity(request, username):
    """
    View for displaying user activity.

    Displays the posts on which the user has voted or commented.

    **Context**
    ``liked_posts``
        A queryset of posts marked as not silly by the user.
    ``silly_posts``
        A queryset of posts marked as silly by the user.
    ``more_posts``
        A queryset of posts marked as more information by the user.
    ``commented_posts``
        A queryset of posts on which the user has commented.

    **Template**
    :template:`user_activity.html`
    """
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
    """
    View for editing user profile.

    Allows authenticated users to edit their own profile information.

    **Context**
    ``form``
        The UserProfileForm instance.

    **Template**
    :template:`edit_profile.html`
    """
    user_profile = request.user.userprofile

    if request.method == 'POST':
        form = UserProfileForm(
                request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile', username=request.user.username)
    else:
        form = UserProfileForm(instance=user_profile)
    return render(request, 'edit_profile.html', {'form': form})