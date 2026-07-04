from django.shortcuts import render, redirect, get_object_or_404
from .models import Appointment
from doctors.models import Doctor
from patients.models import Patient

def appointment_list(request):
    appointments = Appointment.objects.all().order_by('-appointment_date')
    return render(request, 'appointments/list.html', {'appointments': appointments})

def appointment_create(request):
    if request.method == 'POST':
        patient_id = request.POST.get('patient_id')
        doctor_id = request.POST.get('doctor_id')
        medical_record_number = request.POST.get('medical_record_number')
        appointment_date = request.POST.get('appointment_date')
        reason_for_visit = request.POST.get('reason_for_visit')
        priority_level = request.POST.get('priority_level')
        insurance_provider = request.POST.get('insurance_provider')
        allergies = request.POST.get('allergies')
        
        if patient_id and appointment_date:
            Appointment.objects.create(
                patient_id=patient_id,
                doctor_id=doctor_id if doctor_id else None,
                medical_record_number=medical_record_number,
                appointment_date=appointment_date,
                reason_for_visit=reason_for_visit,
                priority_level=priority_level if priority_level else 'Routine',
                insurance_provider=insurance_provider,
                allergies=allergies
            )
            return redirect('appointment_list')
            
    doctors = Doctor.objects.all()
    patients = Patient.objects.all()
    return render(request, 'appointments/add.html', {'doctors': doctors, 'patients': patients})

def appointment_update(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    
    if request.method == 'POST':
        patient_id = request.POST.get('patient_id')
        doctor_id = request.POST.get('doctor_id')
        
        appointment.patient_id = patient_id
        appointment.doctor_id = doctor_id if doctor_id else None
        appointment.medical_record_number = request.POST.get('medical_record_number')
        appointment.appointment_date = request.POST.get('appointment_date')
        appointment.reason_for_visit = request.POST.get('reason_for_visit')
        
        priority_level = request.POST.get('priority_level')
        appointment.priority_level = priority_level if priority_level else 'Routine'
        
        appointment.insurance_provider = request.POST.get('insurance_provider')
        appointment.allergies = request.POST.get('allergies')
        
        status = request.POST.get('status')
        if status:
            appointment.status = status
            
        appointment.save()
        return redirect('appointment_list')
        
    doctors = Doctor.objects.all()
    patients = Patient.objects.all()
    
    return render(request, 'appointments/edit.html', {
        'appointment': appointment,
        'doctors': doctors,
        'patients': patients
    })

def appointment_delete(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        appointment.delete()
        return redirect('appointment_list')
    return render(request, 'appointments/delete.html', {'appointment': appointment})

def appointment_quick_status(request, pk, status):
    appointment = get_object_or_404(Appointment, pk=pk)
    if status in dict(Appointment.STATUS_CHOICES):
        appointment.status = status
        appointment.save()
    return redirect('appointment_list')

def appointment_quick_status_post(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        status = request.POST.get('status')
        if status in dict(Appointment.STATUS_CHOICES):
            appointment.status = status
            appointment.save()
    return redirect('appointment_list')
