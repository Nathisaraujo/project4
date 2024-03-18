from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment

# admin option for Posts from Code Institue Walkthrough - with modifications


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on', 'author')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


# admin option for Comments from Code Institue Walkthrough - with modifications


@admin.register(Comment)
class Comment(SummernoteModelAdmin):

    list_display = ('body', 'author', 'approved')
    search_fields = ['body', 'author']
    list_filter = ('approved',)
