from django import forms
from .models import Comment, Post

# Comment Form from Code Institue Walkthrough
# - added function to limit the characters


class CommentForm(forms.ModelForm):
    """
    Form for submitting comments on posts.

    This form allows users to submit comments on posts.
    It limits the length of the comment body to 500 characters.
    """
    class Meta:
        model = Comment
        fields = ('body',)

        def clean_comment(self):
            body = self.cleaned_data.get('body')
            if body and len(bio) > 500:
                body = body[:500]
                self.cleaned_data['body'] = body
                raise forms.ValidationError("Maximum 500 characters.")
            return body
