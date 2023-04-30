from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import NameForm

# Create your views here.


def index(request):
    send_mail(
        'View your offer',
        'Your TA application has been accepted!',
        'bctaapp@gmail.com',
        ['fanje@bc.edu'],
        fail_silently = False
    )
    return render(request, 'send/index.html')

def send_email(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            body = form.cleaned_data['body']
            recipient = form.cleaned_data['recipient']
            send_mail(
                subject,
                body,
                'bctaapp@gmail.com',
                [recipient],
                fail_silently=False
            )
            return render(request, 'send/index.html')
    else:
        form = NameForm()
    return render(request, 'send/emailform.html', {'form': form})



