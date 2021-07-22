from django.urls import path

from .views import doctordashview, doctorpatientview, doctorsearchview

urlpatterns = [
    path('dash/', doctordashview, name = "doctor-dash"),
    path('patient/', doctorpatientview, name = "doctor-patient"),
    path('search/', doctorsearchview, name = "doctor-search"),
    
]