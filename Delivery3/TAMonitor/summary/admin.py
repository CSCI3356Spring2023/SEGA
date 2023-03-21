from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Course

# Register your models here.
# DataFlair

class CourseAdminForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('Name', 'CourseID', 'Instructor', 'SeatData', 'Rooms', 'Times')

class CourseAdmin(admin.ModelAdmin):
    list_display = ('Name', 'CourseID', 'Instructor', 'SeatData', 'Rooms', 'Times', 'TAs')
    list_filter = ('Name', 'CourseID', 'Instructor', 'SeatData', 'Rooms', 'Times', 'TAs')
    form = CourseAdminForm


admin.site.register(Course, CourseAdmin)
admin.site.unregister(Group)
admin.site.site_header = "Boston College"
