from .models import CollaborateRequest
from django import forms


class CollaborateForm(forms.ModelForm):
    title = forms.CharField(max_length=100)

    class Meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'title','message')