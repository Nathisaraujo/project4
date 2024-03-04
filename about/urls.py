from django.urls import path
from .views import views

urlpatterns = [
    path('<str:username>/', views.ProfileView.as_view(), name='profile'),
] 