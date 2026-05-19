from django.shortcuts import render
from patients.models import Patient
from doctors.models import Doctor
from appointments.models import Appointment

def dashboard(request):
    total_patients = Patient.objects.count()
    total_doctors = Doctor.objects.count()
    total_appointments = Appointment.objects.count()
    
    # Get 5 upcoming or most recently added appointments
    recent_appointments = Appointment.objects.all().order_by('-appointment_date')[:5]
    
    context = {
        'total_patients': total_patients,
        'total_doctors': total_doctors,
        'total_appointments': total_appointments,
        'recent_appointments': recent_appointments,
    }
    
    return render(request, 'dashboard.html', context)
