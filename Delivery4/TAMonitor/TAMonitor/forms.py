from django.forms import ModelForm, TextInput, PasswordInput, Select
from django import forms
from summary.models import Account, Student, Instructor, Admin


class RegisterForm(forms.ModelForm):
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

class StudentRegisterForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["firstname", "lastname", "bcemail", "password", "year_in_school", "major", "eagleid", "work"]
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
            'year_in_school': Select(),
            'major': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Major'
                }),
            'eagleid': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'EalgeID'
                }),
            'work': Select(),
        }

class InstructorRegisterForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = ["firstname", "lastname", "bcemail", "password", "position"]
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
             'position': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Positions e.g CS Professor'
            }),
        }

