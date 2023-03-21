from django.forms import ModelForm, TextInput, PasswordInput, Select
from django import forms
from summary.models import Account


class RegisterForm(forms.ModelForm):
    #username = forms.CharField(max_length=64)
    class Meta:
        model = Account
        fields = ["firstname", "lastname", "bcemail", "password", "permissions"]
        widgets = {
            'firstname': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'First Name'
                }),
            'lastname': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Last Name'
                }),
            'bcemail': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'BC Email'
                }),
            'password': PasswordInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Password'
                }),
            'permissions': Select(),
        }
