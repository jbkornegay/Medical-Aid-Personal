from django.db import models
from django.db.models.base import ModelState
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey
from django.urls import reverse

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

    def __str__(self):
        return self.name

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

    def __str__(self):
        return self.name
    

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

    def __str__(self):
        return self.first_name

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

    def __str__(self):
        return self.first_name


class Feedback(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.first_name

class Support(models.Model):
    fullname = models.CharField(max_length=150)
    email = models.EmailField()
    complaint = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.fullname

class Comment(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse('homepage')

class Faq(models.Model):
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=200)

    def __str__(self):
        return self.question

class Post(models.Model):
    title= models.CharField(max_length=300, unique=True)
    content= models.TextField()

    def __str__(self):
        return self.title
