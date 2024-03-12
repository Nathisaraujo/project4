from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('body',) 

        def clean_comment(self):
            body = self.cleaned_data.get('body')
            if body and len(bio) > 255:
                body = body[:255]
                self.cleaned_data['body'] = body
                raise forms.ValidationError("Bio can't exceed 250 characteres.")
            return body