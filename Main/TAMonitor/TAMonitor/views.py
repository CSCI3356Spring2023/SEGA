from django.shortcuts import render, redirect
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import UpdateView, CreateView
from django.views.generic.detail import DetailView
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

class createcourse(CreateView):
    model = Course
    fields = ["Instructor", "CourseID", "Name", "Description", "SeatData", "Rooms", "Times", "TAs", "WithDiscussion", "GradedInMeeting", "OfficeHours", "ExtraInfo"]

class courseupdate(UpdateView):
    model = Course
    fields = ["Instructor", "CourseID", "Name", "Description", "SeatData", "Rooms", "Times", "TAs", "WithDiscussion", "GradedInMeeting", "OfficeHours", "ExtraInfo"]
    template_name_suffix = '_update_form'

class coursedetailview(DetailView):
    model = Course

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
            student = Student.objects.get(email=user.email)
        selected_course = response.POST.get('selected_course')
        course = Course.objects.get(pk=selected_course)
        apps = Application.objects.filter(account=user)
        app_count = len(apps)

        if form.is_valid() and app_count < 5:
            application = Application.objects.create(
                    account = response.user,
                    SelectedCourse = course,
                    Experience = response.POST.get('experience'),
                    Resume = response.POST.get('resume'),
                    )
            course.Applications.add(application)
            course.save()
            if user.is_student:
                # Add application to student's list of applications
                student.applications.add(application)
                student.save()
        else:
            print("Application Error")
        return redirect('/')
    else:
        form = ApplicationForm()

    return render(response, 'application.html', {'form':form})
