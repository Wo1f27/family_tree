from django.contrib import admin

from .models import Person, Email, PhoneNumber


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'created', 'updated', 'deleted']
    list_filter = ['created', 'updated', 'deleted']
    ordering = ['-created']


@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ['email', 'person', 'is_primary']
    list_filter = ['person']


@admin.register(PhoneNumber)
class PhoneNumberAdmin(admin.ModelAdmin):
    list_display = ['phone_number', 'person', 'is_primary']
    list_filter = ['person']