from django.contrib import admin
from .models import CollaborateRequest

# admin option for the collaboration form from Code Institue Walkthrough
# - with modifications


@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'title', 'message', 'posted')

    def mark_as_posted(self, request, queryset):
        queryset.update(posted=True)
    mark_as_posted.short_description = "Mark selected collaborations as posted"

    actions = ['mark_as_posted']
