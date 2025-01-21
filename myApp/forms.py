from django import forms
from .models import Talent

class TalentForm(forms.ModelForm):
    class Meta:
        model = Talent
        fields = ['name', 'email', 'phone', 'skills', 'description', 'profile_photo']
