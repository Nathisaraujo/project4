from django import forms
from crispy_bootstrap5.bootstrap5 import FloatingField
from .models import CollaborateRequest


# Collaboration form from Code Institue Walkthrough - with modification
class CollaborateForm(forms.ModelForm):
    """
    Form for submitting collaboration requests.

    This form allows users to submit anonimous stories by providing
    their name, email, title, and message.

    **Model**
    :model:`your_app_name.CollaborateRequest`
    """
    title = forms.CharField(max_length=100)

    class Meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'title', 'message')
        