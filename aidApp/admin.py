from django.contrib import admin
from .models import Pharmacy, Clinic, Doctor, Patient, Feedback

# Register your models here.

admin.site.register(Pharmacy)
admin.site.register(Clinic)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Feedback)
