from django.contrib import admin
from .models import Patient, BloodBank, BloodDonor
from unfold.admin import ModelAdmin


@admin.register(Patient)
class CustomAdminClass(ModelAdmin):
    list_display = ('first_name', 'surname', 'date_of_Birth', 'gender', 'blood_group', 'phone_number',
                    'medical_Conditions')
    search_fields = ['first_name', 'surname', 'dob', 'gender', 'blood_group']
    list_filter = ['blood_group', 'gender']


@admin.register(BloodBank)
class CustomAdminClass(ModelAdmin):
    list_display = ('name', 'blood_quantity_in_pints', 'address')
    search_fields = ['name', 'blood_quantity_in_pints', 'address']


@admin.register(BloodDonor)
class CustomAdminClass(ModelAdmin):
    list_display = ('name', 'blood_group', 'address', 'gender', 'phone_number', 'eligible_to_donate')
    search_fields = ['name', 'blood_group', 'address', 'gender', 'phone_number', 'date_of_donation']
    list_filter = ['blood_group', 'gender']
