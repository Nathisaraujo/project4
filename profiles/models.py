from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return self.user.username

class UsersPostRequest(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100, default='Default Title') 
    message = models.TextField()
    excerpt = models.TextField(max_length=200, blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Collaboration request from {self.name}"