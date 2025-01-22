from django import forms
from .models import Talent

class TalentForm(forms.ModelForm):
    class Meta:
        model = Talent
        fields = ['name', 'email', 'phone', 'skills', 'description', 'profile_photo']
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Your Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'input-field', 'placeholder': 'Your Email Address'}),
            'phone': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Your Phone Number'}),
            'skills': forms.Textarea(attrs={'class': 'input-field', 'placeholder': 'Your Skills and Expertise', 'rows': 4}),
            'description': forms.Textarea(attrs={'class': 'input-field', 'placeholder': 'A brief description about you', 'rows': 4}),
            'profile_photo': forms.ClearableFileInput(attrs={'class': 'input-field'}),
        }
