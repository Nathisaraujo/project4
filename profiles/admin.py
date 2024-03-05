from django.contrib import admin
from .models import UserProfile, UsersPostRequest 


# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'bio']

@admin.register(UsersPostRequest)
class UsersPostRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'message')  

    def mark_as_posted(self, request, queryset):
        queryset.update(posted=True)
    mark_as_posted.short_description = "Mark selected collaborations as posted"

    actions = ['mark_as_posted']
