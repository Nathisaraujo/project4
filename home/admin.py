from django.contrib import admin
from .models import CollaborateRequest

# admin option for the collaboration form from Code Institue Walkthrough
# - with modifications


@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):
    """
    Admin interface for managing collaboration requests.

    This admin class provides options for viewing, filtering, and marking
    collaboration requests as posted.

    **Model**
    :model:`your_app_name.CollaborateRequest`

    **Actions**
    - Mark selected collaborations as posted
    """
    list_display = ('name', 'email', 'title', 'message', 'posted')

    def mark_as_posted(self, request, queryset):
        """
        Action to mark selected collaborations as posted.

        This method updates the 'posted' attribute of selected collaboration
        requests to mark them as posted.

        **Model**
        :model:`your_app_name.CollaborateRequest`
        """
        queryset.update(posted=True)
    mark_as_posted.short_description = "Mark selected collaborations as posted"

    actions = ['mark_as_posted']
