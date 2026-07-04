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
from patients.views import patient_list, patient_create, patient_update, patient_delete
from doctors.views import doctor_list, doctor_create, doctor_update, doctor_delete
from appointments.views import appointment_list, appointment_create, appointment_update, appointment_delete, appointment_quick_status, appointment_quick_status_post

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name='dashboard'),
    
    # Patients App
    path('patients/', patient_list, name='patient_list'),
    path('patients/add/', patient_create, name='patient_create'),
    path('patients/<int:pk>/edit/', patient_update, name='patient_update'),
    path('patients/<int:pk>/delete/', patient_delete, name='patient_delete'),

    
    # Doctors App
    path('doctors/', doctor_list, name='doctor_list'),
    path('doctors/add/', doctor_create, name='doctor_create'),
    path('doctors/<int:pk>/edit/', doctor_update, name='doctor_update'),
    path('doctors/<int:pk>/delete/', doctor_delete, name='doctor_delete'),
    
    # Appointments App
    path('appointments/', appointment_list, name='appointment_list'),
    path('appointments/add/', appointment_create, name='appointment_create'),
    path('appointments/<int:pk>/edit/', appointment_update, name='appointment_update'),
    path('appointments/<int:pk>/delete/', appointment_delete, name='appointment_delete'),
    path('appointments/<int:pk>/status/<str:status>/', appointment_quick_status, name='appointment_quick_status'),
    path('appointments/<int:pk>/status-update/', appointment_quick_status_post, name='appointment_quick_status_post'),
]

