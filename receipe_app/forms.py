from django import forms
from .models import User, Receipe

class UserRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'nameid'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control', 'id': 'emailid'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control', 'id': 'passwordid'
            })
        }


class ReceipeForm(forms.ModelForm):
    class Meta:
        model = Receipe
        fields = ['name', 'description', 'image']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'nameid'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control', 'id': 'descriptionid'
            }),
        }