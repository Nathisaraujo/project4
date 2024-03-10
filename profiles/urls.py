from . import views
from django.urls import path


urlpatterns = [
    path('<str:username>/', views.profile, name='profile'),
    #urls da colega
    path('profile/<str:username>/add_post/', views.AddPost.as_view(), name='add_post'),
    path('post/edit/<slug:slug>/', views.EditPost.as_view(), name='update_post'),
    path('delete/<slug:slug>/remove', views.DeletePost.as_view(), name='delete_post'),
    # my urls
    path('manage/<str:username>/manage_posts', views.ManagePosts, name='user_posts'),
    path('history/<str:username>/liked-posts/', views.user_activity, name='liked_posts'),
]