from django.contrib import admin
from .models import Home, CollaborateRequest
# from django_summernote.admin import SummernoteModelAdmin


# @admin.register(Home)
# class HomeAdmin(SummernoteModelAdmin):
#     summernote_fields = ('content',)

# Note: admin.ModelAdmin is the standard way of registering
#       our model with the admin panel. We do it differently
#       above because we are supplying Summernote fields.
#       If you want to customise the admin panel view in your
#       own projects, then inherit from admin.ModelAdmin like
#       we do below.

@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'title', 'message', 'posted')  

    def mark_as_posted(self, request, queryset):
        queryset.update(posted=True)
    mark_as_posted.short_description = "Mark selected collaborations as posted"

    actions = ['mark_as_posted']

    