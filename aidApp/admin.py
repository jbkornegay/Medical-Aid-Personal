from django.contrib import admin
from .models import Pharmacy, Clinic, Doctor, Patient, Feedback, Faq, Comment, Post, Support

# Register your models here.

admin.site.register(Pharmacy)
admin.site.register(Clinic)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Feedback)
admin.site.register(Faq)
admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(Support)