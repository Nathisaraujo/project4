from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import UserProfile
from blog.models import Post

# admin option for the User Profile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """
    Admin interface for managing user profiles.

    This admin class provides options for viewing and managing user profiles.

    **Model**
    :model:`your_app_name.UserProfile`
    """
    list_display = ['user', 'bio']

# admin option for the add post model - from Bawarchi Khana's code


class PostAdmin(SummernoteModelAdmin):
    """
    Admin interface for managing blog posts.

    This admin class provides options for viewing, searching, filtering, and
    managing blog posts. It also integrates with Summernote for rich text 
    editing.

    **Model**
    :model:`blog.Post`

    **Actions**
    - Approve selected posts
    """

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
    actions = ['approve_posts']

    def approve_posts(self, request, queryset):
        queryset.update(approved=True)
