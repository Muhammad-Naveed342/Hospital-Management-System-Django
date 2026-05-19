from django.shortcuts import render, redirect
from .models import Appointment

def appointment_list(request):
    appointments = Appointment.objects.all().order_by('-appointment_date')
    return render(request, 'appointments/list.html', {'appointments': appointments})

def appointment_create(request):
    if request.method == 'POST':
        patient_name = request.POST.get('patient_name')
        appointment_date = request.POST.get('appointment_date')
        
        if patient_name and appointment_date:
            Appointment.objects.create(
                patient_name=patient_name,
                appointment_date=appointment_date
            )
            return redirect('appointment_list')
            
    return render(request, 'appointments/add.html')

