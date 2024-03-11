from django import forms
#imports da colega
from blog.models import Post
from .models import UserProfile
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

#forms da colega
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'excerpt',
        ]
        widgets = {
            'content': SummernoteWidget(),
                    }

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'birth_date', 'location', 'gender', 'picture']