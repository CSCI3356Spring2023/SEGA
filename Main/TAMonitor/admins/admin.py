from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from summary.models import Course, Account, Student, Instructor, Admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import gettext_lazy as _

@admin.register(Account)
class UserAdmin(DjangoUserAdmin):
    """Define admin model for custom User model with no email field."""

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('firstname', 'lastname')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)


admin.site.register(Student)
admin.site.register(Instructor)
admin.site.register(Admin)
admin.site.register(Course)
admin.site.unregister(Group)
admin.site.site_header = "Boston College TA Application System Overview"
