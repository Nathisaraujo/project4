from django.contrib import admin
from .models import Post, Comment 
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(Post) 
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on', 'author')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

@admin.register(Comment)
class Comment(SummernoteModelAdmin):

    list_display = ('body', 'author', 'approved')
    search_fields = ['body', 'author']
    list_filter = ('approved',)

