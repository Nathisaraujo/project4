from django import forms
from crispy_bootstrap5.bootstrap5 import FloatingField
from .models import CollaborateRequest


# Collaboration form from Code Institue Walkthrough - with modification
class CollaborateForm(forms.ModelForm):
    title = forms.CharField(max_length=100)

    class Meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'title', 'message')
        