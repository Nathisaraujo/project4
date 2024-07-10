from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment

# admin option for Posts from Code Institue Walkthrough - with modifications


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Customizes the admin interface for Post model.

    This admin option allows managing Post instances including fields such as
    title, slug, status, created_on, and author. It enables rich text editing
    for the content field using the Summernote editor.
    """

    list_display = ('title', 'slug', 'status', 'created_on', 'author')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

    # Fixing assessments error - ensuring it handles updating the status field
    def approve_posts(self, request, queryset):
        for post in queryset:
            post.publish()
        self.message_user(request, "Selected posts have been approved and published.")
    approve_posts.short_description = 'Approve and publish selected posts'


# admin option for Comments from Code Institue Walkthrough - with modifications


@admin.register(Comment)
class Comment(SummernoteModelAdmin):
    """
    Customizes the admin interface for Comment model.

    This admin option allows managing Comment instances including fields such
    as body, author, and approved. It enables rich text editing for the body
    field using the Summernote editor.
    """

    list_display = ('body', 'author', 'approved')
    search_fields = ['body', 'author']
    list_filter = ('approved',)
