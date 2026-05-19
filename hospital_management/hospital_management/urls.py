"""
URL configuration for hospital_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hospital_management.views import dashboard
from patients.views import patient_list, patient_create
from doctors.views import doctor_list, doctor_create
from appointments.views import appointment_list, appointment_create

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name='dashboard'),
    
    # Patients App
    path('patients/', patient_list, name='patient_list'),
    path('patients/add/', patient_create, name='patient_create'),
    
    # Doctors App
    path('doctors/', doctor_list, name='doctor_list'),
    path('doctors/add/', doctor_create, name='doctor_create'),
    
    # Appointments App
    path('appointments/', appointment_list, name='appointment_list'),
    path('appointments/add/', appointment_create, name='appointment_create'),
]

