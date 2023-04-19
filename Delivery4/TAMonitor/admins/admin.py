from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from summary.models import Course, Account, Student, Instructor, Admin


admin.site.register(Student)
admin.site.register(Instructor)
admin.site.register(Admin)
admin.site.register(Course)
admin.site.unregister(Group)
admin.site.site_header = "Boston College TA Application System Overview"
