from django.contrib import admin
from .models import UserProfile
from blog.models import Post
#import da colega
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'bio']


class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
    actions = ['approve_posts']

    def approve_posts(self, request, queryset):
        queryset.update(approved=True)
