from django import forms
from .models import UsersPostRequest
from crispy_bootstrap5.bootstrap5 import FloatingField

class UsersPostForm(forms.ModelForm):
    title = forms.CharField(max_length=100)

    class Meta:
        model = UsersPostRequest
        fields = ('name', 'title','message')