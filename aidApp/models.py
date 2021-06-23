from django.db import models
from django.db.models.base import ModelState
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Pharmacy(models.Model):
    name = models.CharField(max_length = 100)
    street_address = models.CharField(max_length = 100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.IntegerField()
    phone_number = models.IntegerField()
    days_open = models.CharField(max_length=100)
    open_time = models.TimeField()
    close_time = models.TimeField()
    website = models.CharField(max_length=100)

class Clinic(models.Model):
    name = models.CharField(max_length = 100)
    street_address = models.CharField(max_length = 100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.IntegerField()
    phone_number = models.IntegerField()
    days_open = models.CharField(max_length=100)
    open_time = models.TimeField()
    close_time = models.TimeField()
    

class Doctor(models.Model):
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    street_address = models.CharField(max_length = 100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.IntegerField()
    phone_number = models.IntegerField()
    specialty = models.CharField(max_length=50)

class Patient(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=25)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.IntegerField
    appointments = models.DateTimeField
    insurance = models.CharField(max_length=50)

class Feedback(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=500)
    