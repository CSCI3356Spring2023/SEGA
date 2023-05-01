from django.shortcuts import render, redirect
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
import os

from .forms import StudentRegisterForm, InstructorRegisterForm, AdminRegisterForm, ApplicationForm, CreateCourseForm
from summary.models import Account, Student, Instructor, Admin, Course, Application

def home(response):
    courses = Course.objects.all()
    return render(response, 'home.html', {'courses':courses})

def logout_view(request):
    logout(request)
    return render(request, 'home.html')

def register(request):
    return render(request, 'register.html')

def studentregister(request):
    if request.method == 'POST':
        form = StudentRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = StudentRegisterForm()

    context = {'form': form}
    return render(request, 'studentregister.html', context)

def instructorregister(request):
    if request.method == 'POST':
        form = InstructorRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = InstructorRegisterForm()

    context = {'form': form}
    return render(request, 'instructorregister.html', context)

def adminregister(request):
    if request.method == 'POST':
        form = AdminRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AdminRegisterForm()

    context = {'form': form}
    return render(request, 'adminregister.html', context)

def createcourse(request):
    if request.method == 'POST':
        form = CreateCourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CreateCourseForm()

    context = {'form': form}
    return render(request, 'createcourse.html', context)

def instructorsummary(request):
    # Needs implementation
    return render(request, 'instructorsummary.html')

class CreateApplication(CreateView):
    model = Application
    form_class = ApplicationForm()
    template_name = 'application.html'

    def save(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()


def apply(response):
    if response.method == 'POST':
        form = ApplicationForm(response.POST, response.FILES)
        user = response.user
        if user.is_student:
            student = Student.objects.get(user=user)
        course = Course.objects.get(id=id)
        apps = Application.objects.filter(user=user)
        app_count = len(apps)

        if form.is_valid() and app_count < 5:
            application = Application(course_id = course.CourseID, user = response.user)
            resume = response.FILES['resume']
            application.resume = resume
            application.save()
            course.application.add(application)
            course.save()
            if user.is_student:
                print("is student")
                # Add application to student's list of applications
        else:
            print("Application Error")
        return redirect('/')
    else:
        form = ApplicationForm()

    return render(response, 'application.html', {'form':form})
