from django import forms
from django.forms import ModelForm
from summary.models import Account

class RegisterForms(ModelForm):
    firstname = forms.CharField(max_length = 64)
    lastname = forms.CharField(max_length = 64)
    bcemail = forms.CharField(max_length = 64)
    password = forms.CharField(widget=PasswordInput)
    email = forms.CharField(widget=EmailInput)
    position = forms.CharField(max_length=16, choices=PERMISSIONS, default='Student')

    class Meta:
        model = Account
        fields = ['firstname', 'lastname', 'password', 'bcemail', 'position']

