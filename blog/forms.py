from django import forms
from .models import Comment, Post

# Comment Form from Code Institue Walkthrough
# - added function to limit the characters


class CommentForm(forms.ModelForm):
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

# Post Form with functions to limit the characters of title and excerpt


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('excerpt', 'title')

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
