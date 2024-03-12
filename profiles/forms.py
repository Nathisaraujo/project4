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
            'excerpt',
            'content',
        ]
        widgets = {
            'content': SummernoteWidget(),
                    }

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
    


