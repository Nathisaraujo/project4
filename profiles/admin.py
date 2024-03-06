from django.contrib import admin
from .models import UserProfile, UsersPostRequest 


# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'bio']

@admin.register(UsersPostRequest)
class UsersPostRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'excerpt', 'message', 'created_on',  'approved' ) 
    list_filter = ('approved',) 
    actions = ['approve_posts']

    def approve_posts(self, request, queryset):
        queryset.update(approved=True)
    
    approve_posts.short_description = "Approve selected posts"

