from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from . forms import RegisterForm
from summary.models import Account

def index(request):
    return HttpResponse("Welcome! Please navigate to /admin or /register or /createcourse")

def register(response):
    form = RegisterForm(response.POST)
    if response.method == 'POST':
        form_class = RegisterForm(response.POST)
        if form_class.is_valid():
            account = form.save()
            account.refresh_from_db()
            account.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            account = authenticate(username=username, password=password)
            login(response, user)

            return redirect('/')

        else:
         form = RegisterForm()

    return render(response, 'register.html', {'form': form})
