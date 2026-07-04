from django.shortcuts import render
from patients.models import Patient
from doctors.models import Doctor
from appointments.models import Appointment

def dashboard(request):
    total_patients = Patient.objects.count()
    total_doctors = Doctor.objects.count()
    total_appointments = Appointment.objects.count()
    
    # Get 4 most recent appointments for dashboard
    recent_appointments = Appointment.objects.all().order_by('-appointment_date')[:4]
    
    context = {
        'total_patients': total_patients,
        'total_doctors': total_doctors,
        'total_appointments': total_appointments,
        'recent_appointments': recent_appointments,
    }
    
    return render(request, 'dashboard.html', context)
