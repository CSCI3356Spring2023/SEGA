from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    fullname = forms.CharField(label="Full name")
    role = forms.ChoiceField(widget = forms.RadioSelect, choices = [('Teacher,', 'Teacher'), ('Student', 'Student'), ('Admin', 'Admin')]
    )

    class Meta:
        model= User
        fields = ['role', 'username', 'password1', 'password2']

    def __init__(self, *args, **kwargs): 
        super(RegisterForm, self).__init__( *args, **kwargs)