from . import views
from django.urls import path, include
from .views import like_post
from django.contrib import admin

urlpatterns = [
    path('', views.PostList.as_view(), name='sillytalks'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
    path('<slug:slug>/like/', views.like_post, name='like-post'),
    path('accounts/', include('allauth.urls')),
]