from django.urls import path, include
from django.contrib import admin
from . import views
from .views import PostVote


urlpatterns = [
    path('search/', views.search_view, name='search'),
    path('', views.PostList.as_view(), name='sillytalks'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
    path('vote/<slug:slug>', PostVote.as_view(), name='post_vote'),
    path('accounts/', include('allauth.urls')),
]