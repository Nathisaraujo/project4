from django import forms
from django.forms import Textarea
from blog.models import Post
from .models import UserProfile

# Post form - from Bawarchi Khana's code - with modifications


class PostForm(forms.ModelForm):
    """
    Form for adding and editing blog posts.

    This form allows users to add and edit blog posts, specifying
    the title, excerpt, and content of the post. It limits the length of the post title to 200 characters
    and the post excerpt to 500 characters.

    **Model**
    :model:`blog.Post`

    **Fields**
    - title: title of the post
    - excerpt: text summarizing the post
    - content: text of the post
    """
    class Meta:
        model = Post
        fields = [
            'title',
            'excerpt',
            'content',
        ]
        
        def clean_excerpt(self):
            excerpt = self.cleaned_data.get('excerpt')
            if excerpt and len(excerpt) > 500:
                excerpt = excerpt[:500]
                self.cleaned_data['excerpt'] = excerpt
                raise forms.ValidationError("Maximum 500 characters.")
            return bio

        def clean_title(self):
            title = self.cleaned_data.get('title')
            if title and len(bio) > 200:
                title = title[:200]
                self.cleaned_data['title'] = title
                raise forms.ValidationError("Maximum 200 characters.")
            return bio

# User Profile Form with a function to limit the characters of bio


class UserProfileForm(forms.ModelForm):
    """
    Form for updating user profiles.

    This form allows users to update their profiles, including
    their bio, birth date, location, gender, and profile picture.

    **Model**
    :model:`your_app_name.UserProfile`

    **Fields**
    - bio: piece of text the user can write about himself
    - birth_date: date of birth
    - location: where the user is located
    - gender: user's gender
    - picture: user's profile photo
    """
    class Meta:
        model = UserProfile
        fields = ['bio', 'birth_date', 'location', 'gender', 'picture']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_bio(self):
        bio = self.cleaned_data.get('bio')
        if bio and len(bio) > 255:
            bio = bio[:255]
            self.cleaned_data['bio'] = bio
            raise forms.ValidationError("Bio can't exceed 250 characteres.")
        return bio
