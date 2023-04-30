from django import forms


#class NameForm(forms.Form):
   # subject = forms.CharField(max_length=100)
   # body = forms.CharField(max_length=1000)
   # recipient = forms.CharField(max_length = 100)

class NameForm(forms.Form):
    subject = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Enter a subject'}),
    )
    recipient = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Enter the recipient email'}),
    )
    body = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Enter the message body'}),
    )
    def clean_recipient(self):
        recipient = self.cleaned_data['recipient'].lower()  # Convert to lowercase
        if not recipient.endswith('@bc.edu') and not recipient.endswith('@bc.edu'):
            raise forms.ValidationError("The email address must end with '@bc.edu'")
        return recipient
