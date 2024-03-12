from django import forms
from django.utils.translation import gettext_lazy as _
# from bootstrap_datepicker_plus import DatePickerInput
#imports da colega
from blog.models import Post
from .models import UserProfile
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

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'birth_date', 'location', 'gender', 'picture']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['birth_date'].label = _('Birth Date')
            self.fields['birth_date'].help_text = _('Select your birth date from the calendar.')

