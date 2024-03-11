from django.db import models
from django.contrib.auth.models import User
from blog.models import Post
from django.utils import timezone

# Create your models here.
GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
]

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True)
    last_login_date = models.DateTimeField(blank=True, null=True)
    registration_date = models.DateTimeField(default=timezone.now)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True)

    def __str__(self):
        return self.user.username