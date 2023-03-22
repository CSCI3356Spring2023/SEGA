# from django.http import HttpResponse
# from django.shortcuts import render
# from django.contrib.auth import authenticate, login
# from . forms import RegisterForm
# from summary.models import Account

from django.contrib.auth import authenticate, login, logout
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
            # username = form.cleaned_data.get('username')
            # password = form.cleaned_data.get('password1')
            # account = authenticate(username=username, password=password)
            # login(response, account)

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
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'home.html',{})
        else:
            # handle invalid login credentials
            # for example:
            error_message = "Invalid username or password"
            return render(request, 'login.html', {'error_message': error_message})
    else:
        # handle GET request to show login form
        return render(request, 'login.html')
