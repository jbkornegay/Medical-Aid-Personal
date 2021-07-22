from django.shortcuts import render
from aidApp.models import Doctor
from django.contrib.auth.decorators import login_required

# Create your views here

def doctordashview(request):
    return render(request, 'doctor/doctor-dash.html')

def doctorpatientview(request):
    return render(request, 'doctor/doctor-patient.html')

def doctorsearchview(request):
    return render(request, 'doctor/doctor-search.html')