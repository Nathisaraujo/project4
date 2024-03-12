from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('body',) 

        def clean_comment(self):
            body = self.cleaned_data.get('body')
            if body and len(bio) > 500:
                body = body[:500]
                self.cleaned_data['body'] = body
                raise forms.ValidationError("Comment can't exceed 500 characteres.")
            return body
        
    def clean_excerpt(self):
        bio = self.cleaned_data.get('excerpt')
        if bio and len(bio) > 500:
            bio = bio[:500]
            self.cleaned_data['excerpt'] = excerpt
            raise forms.ValidationError("Excerpt can't exceed 500 characteres.")
        return bio
    
    def clean_title(self):
        bio = self.cleaned_data.get('title')
        if bio and len(bio) > 200:
            bio = bio[:200]
            self.cleaned_data['title'] = title
            raise forms.ValidationError("Title can't exceed 200 characteres.")
        return bio