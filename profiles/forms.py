from django import forms
from django.forms import Textarea
from blog.models import Post
from .models import UserProfile
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

# Add Post form - from Bawarchi Khana's code


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'excerpt',
            'content',
        ]
        widgets = {
            'content': SummernoteWidget(),
                    }

# User Profile Form with a function to limit the characters of bio


class UserProfileForm(forms.ModelForm):
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
