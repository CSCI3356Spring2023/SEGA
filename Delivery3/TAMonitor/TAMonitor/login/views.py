from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.models import User

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
