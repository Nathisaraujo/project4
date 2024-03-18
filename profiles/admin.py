from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import UserProfile
from blog.models import Post

# admin option for the User Profile
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'bio']

# admin option for the add post model - from Bawarchi Khana's code
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
    actions = ['approve_posts']

    def approve_posts(self, request, queryset):
        queryset.update(approved=True)
