from django.contrib import admin
from .models import UserProfile, UsersPostRequest 


# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'bio']

@admin.register(UsersPostRequest)
class UsersPostRequestAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'excerpt', 'content', 'created_on',  'approved' ) 
    list_filter = ('approved',) 
    search_fields = ('name', 'title', 'message')
    actions = ['approve_posts']

    def approve_posts(self, request, queryset):
        queryset.update(approved=True)
        self.message_user(request, "Selected posts have been approved.")
    
    approve_posts.short_description = "Approve selected posts"

