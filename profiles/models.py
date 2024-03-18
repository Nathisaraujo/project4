from django.db import models
from django.utils import timezone
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from blog.models import Post

# Displays the gender choiced for the User Profile
GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
]

# User Profile model


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, max_length=255)
    picture = CloudinaryField('image', default='placeholder')
    birth_date = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True)
    registration_date = models.DateTimeField(default=timezone.now)
    gender = models.CharField(
        max_length=10, choices=GENDER_CHOICES, blank=True
    )

    def __str__(self):
        return self.user.username
