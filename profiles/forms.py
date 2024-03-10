from django import forms
#imports da colega
from blog.models import Post
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