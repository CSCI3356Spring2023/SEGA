# from django.http import HttpResponse
# from django.shortcuts import render
# from django.contrib.auth import authenticate, login
# from . forms import RegisterForm
# from summary.models import Account

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import RegisterForm, InstructorRegisterForm, StudentRegisterForm
from django.contrib.auth.models import User

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
            login(response, account)

            return redirect('/')

        else:
         form = RegisterForm()

    return render(response, 'register.html', {'form': form})

def studentregister(response):
    form = StudentRegisterForm(response.POST)
    if response.method == 'POST':
        form_class = StudentRegisterForm(response.POST)
        if form_class.is_valid():
            account = form.save()
            account.refresh_from_db()
            account.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            account = authenticate(username=username, password=password)
            if account is not None:
                login(response, account)
                # return redirect('/home')

            return redirect('/')

        else:
            form = StudentRegisterForm()

    return render(response, 'studentregister.html', {'form': form})


def instructorregister(response):
    form = InstructorRegisterForm(response.POST)
    if response.method == 'POST':
        form_class = InstructorRegisterForm(response.POST)
        if form_class.is_valid():
            account = form.save()
            account.refresh_from_db()
            account.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            account = authenticate(username=username, password=password)
            if account is not None:
                login(response, account)

            return redirect('/')

        else:
            form = InstructorRegisterForm()

    return render(response, 'instructorregister.html', {'form':form})

def register_view(request):
    if (request.method == "POST"):
        form = RegisterForm(request.Post)#Minji wrote response
        if form.is_valid():
            form.save()
            user = form.get('username')
            password = form.get('password')
            role = form.get('role')
            myRole = User.objects.get_or_create(name=role)
            User.add(myRole)
            User.save()
            form.save()
            if role == 'Student':
                return redirect('/login')

    return render(request, 'login.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(None, data=request.POST)
        if form.is_valid():
            form.clean()
            user = form.get_user()
            if user is not None:
                login(request, user)
                if user.is_superuser:
                    return redirect('/admin')
                return render(request, 'home.html',{})
            else:
                # handle invalid login credentials
                error_message = "Invalid username or password"
                return render(request, 'registration/login.html', {'error_message': error_message})
        else:
            # handle invalid login credentials
            error_message = "Invalid username or password"
            return render(request, 'registration/login.html', {'error_message': error_message, 'form' : form})
    else:
        # handle GET request to show login form
        form = AuthenticationForm(request)
        return render(request, 'registration/login.html', {'form' : form})

def logout_view(request):
    logout(request)
    return render(request, 'home.html')

def profile_view(request):
    return render(request, 'home.html')
