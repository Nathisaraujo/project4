from django import forms
from .models import UsersPostRequest
from crispy_bootstrap5.bootstrap5 import FloatingField

class UsersPostForm(forms.ModelForm):

    class Meta:
        model = UsersPostRequest
        fields = ('name', 'title','excerpt','message')