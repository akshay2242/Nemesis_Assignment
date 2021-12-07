from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

# User Signup form
class CustomUserForm(UserCreationForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput)
    class Meta:
        model = CustomUser
        fields = [ 'username','email', 'address' ]
        
