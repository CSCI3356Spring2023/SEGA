from django.forms import ModelForm, TextInput, PasswordInput, Select
from django import forms
from summary.models import Account, Student, Instructor, Admin, Course, Application
from django.contrib.auth.forms import AuthenticationForm, UsernameField


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ["firstname", "lastname", "email", "password"]
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
            'email': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'BC Email (Username)'
                }),
            'password': PasswordInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Password'
                }),
        }

class StudentRegisterForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ["firstname", "lastname", "email", "password", "year_in_school", "major", "eagleid", "work"]
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
            'email': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'BC Email (Username)'
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
                'placeholder': 'Eagle ID'
                }),
            'work': Select(),
        }
    # def save(self):
    #     Account.is_student = True

class InstructorRegisterForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = ["firstname", "lastname", "email", "password", "position"]
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
            'email': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'BC Email (Username)'
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


class AdminRegisterForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = ["firstname", "lastname", "email", "password", "position"]
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
            'email': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'BC Email (Username)'
                }),
            'password': PasswordInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Password'
                }),
             'position': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Positions e.g IT Admin'
            }),
        }

class ApplicationForm(forms.ModelForm):
    # field_list = [Course.Name for Course in Course._meta.get_fields()]
    course_list = Course.objects.all()
    selected_course = forms.ModelChoiceField(label="Select A Course to Apply For.", queryset=Course.objects.all())
    resume = forms.FileField(label="Upload a resume here.", required=False)
    experience = forms.CharField(label="Describe your previous experience with the course, including any grades you may have recieved.")
    class Meta:
        model = Application
        fields = ["selected_course", "experience", "resume"]

