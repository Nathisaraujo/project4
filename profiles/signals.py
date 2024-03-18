from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserProfile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    Signal receiver to create a user profile when a new user is registered.

    This function creates a UserProfile instance associated with the newly
    registered user when a User instance is created.

    **Parameters**
    - sender: The sender of the signal (User model).
    - instance: The newly created instance (User instance).
    - created: A boolean indicating whether the instance was created.

    **Model**
    :model:`your_app_name.UserProfile`
    """
    if created:
        UserProfile.objects.create(user=instance)


# save profile personal information
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    """
    Signal receiver to save user profile information.

    This function saves the UserProfile instance associated with a user
    when the user instance is saved.

    **Parameters**
    - sender: The sender of the signal (User model).
    - instance: The instance being saved (User instance).

    **Model**
    :model:`your_app_name.UserProfile`
    """
    instance.userprofile.save()
