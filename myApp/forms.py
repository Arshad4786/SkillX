from django import forms
from .models import Talent, Client as ClientModel, HireRequest  # Import HireRequest here

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

    def clean_profile_photo(self):
        photo = self.cleaned_data.get('profile_photo')
        if photo and not photo.name.endswith(('.jpg', '.jpeg', '.png')):
            raise forms.ValidationError("Only .jpg, .jpeg, and .png files are allowed.")
        return photo

# class HireRequestForm(forms.ModelForm):
#     class Meta:
#         model = HireRequest  # Now HireRequest is imported
#         fields = ['client_name', 'client_email', 'message']
        
#         widgets = {
#             'client_name': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Your Name'}),
#             'client_email': forms.EmailInput(attrs={'class': 'input-field', 'placeholder': 'Your Email Address'}),
#             'message': forms.Textarea(attrs={'class': 'input-field', 'placeholder': 'Message or reason for hiring', 'rows': 4}),
#         }
from django import forms
from .models import HireRequest

class HireRequestForm(forms.ModelForm):
    class Meta:
        model = HireRequest
        fields = ['client', 'talent', 'message']  # Use client as ForeignKey field and talent as ForeignKey field
        widgets = {
            'client': forms.Select(attrs={'class': 'input-field'}),  # Dropdown for selecting client
            'talent': forms.Select(attrs={'class': 'input-field'}),  # Dropdown for selecting talent
            'message': forms.Textarea(attrs={'class': 'input-field', 'placeholder': 'Message or reason for hiring', 'rows': 4}),
        }
from django import forms
from .models import Client

class ClientRegistrationForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone', 'address']

    def clean_client_email(self):
        email = self.cleaned_data.get('client_email')
        if not ClientModel.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is not registered. Please sign up first.")
        return email
