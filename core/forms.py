from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

class SignupForm(UserCreationForm):
    contact = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your contact number',  # Placeholder for the input field
        'class': 'w-full py-4 px-6 rounded-xl'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'contact')  # Include 'contact' in the fields

        # Fields are defined here within Meta for customization
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Your username',
                'class': 'w-full py-4 px-6 rounded-xl'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Your email address',
                'class': 'w-full py-4 px-6 rounded-xl'
            }),
            'password1': forms.PasswordInput(attrs={
                'placeholder': 'Your password',
                'class': 'w-full py-4 px-6 rounded-xl'
            }),
            'password2': forms.PasswordInput(attrs={
                'placeholder': 'Repeat password',
                'class': 'w-full py-4 px-6 rounded-xl'
            }),
            'contact': forms.TextInput(attrs={
                'placeholder': 'Your contact number',
                'class': 'w-full py-4 px-6 rounded-xl'
            }),
        }