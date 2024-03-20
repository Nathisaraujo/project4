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
    """
    Model to store user profiles.

    This model represents user profiles, including fields for bio,
    profile picture, birth date, location, registration date,
    and gender.

    **Attributes**
    - user: The associated user object.
    - bio: User's bio information.
    - picture: User's profile picture = CloudinaryField storing pictures
    - birth_date: User's birth date.
    - location: User's location.
    - registration_date: Date and time of user registration.
    - gender: User's gender.

    **Methods**
    - __str__: Returns the username of the associated user.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, max_length=255)
    picture = CloudinaryField('image', null=True, blank=True)
    birth_date = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True)
    registration_date = models.DateTimeField(default=timezone.now)
    gender = models.CharField(
        max_length=10, choices=GENDER_CHOICES, blank=True
    )

    def __str__(self):
        """
        Returns the username of the associated user.
        """
        return self.user.username
