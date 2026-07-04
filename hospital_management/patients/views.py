from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient

def patient_list(request):
    patients = Patient.objects.all().order_by('-id')
    return render(request, 'patients/list.html', {'patients': patients})

def patient_create(request):
    if request.method == 'POST':
        p = request.POST
        name   = p.get('name')
        age    = p.get('age')
        gender = p.get('gender')
        phone  = p.get('phone')
        address = p.get('address')

        if name and age and gender and phone and address:
            Patient.objects.create(
                name=name,
                age=age,
                gender=gender,
                phone=phone,
                address=address,
                date_of_birth=p.get('date_of_birth') or None,
                blood_group=p.get('blood_group') or None,
                marital_status=p.get('marital_status') or None,
                nationality=p.get('nationality'),
                occupation=p.get('occupation'),
                patient_id=p.get('patient_id') or None,
                email=p.get('email') or None,
                emergency_contact_name=p.get('emergency_contact_name'),
                emergency_contact_phone=p.get('emergency_contact_phone'),
                emergency_contact_relation=p.get('emergency_contact_relation'),
                allergies=p.get('allergies'),
                chronic_conditions=p.get('chronic_conditions'),
                current_medications=p.get('current_medications'),
                status=p.get('status') or 'Active',
                insurance_provider=p.get('insurance_provider'),
                insurance_policy_no=p.get('insurance_policy_no'),
            )
            return redirect('patient_list')

    return render(request, 'patients/add.html')

def patient_update(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        p = request.POST
        patient.name             = p.get('name')
        patient.age              = p.get('age')
        patient.gender           = p.get('gender')
        patient.phone            = p.get('phone')
        patient.address          = p.get('address')
        patient.date_of_birth    = p.get('date_of_birth') or None
        patient.blood_group      = p.get('blood_group') or None
        patient.marital_status   = p.get('marital_status') or None
        patient.nationality      = p.get('nationality')
        patient.occupation       = p.get('occupation')
        patient.patient_id       = p.get('patient_id') or None
        patient.email            = p.get('email') or None
        patient.emergency_contact_name     = p.get('emergency_contact_name')
        patient.emergency_contact_phone    = p.get('emergency_contact_phone')
        patient.emergency_contact_relation = p.get('emergency_contact_relation')
        patient.allergies            = p.get('allergies')
        patient.chronic_conditions   = p.get('chronic_conditions')
        patient.current_medications  = p.get('current_medications')
        patient.status               = p.get('status') or 'Active'
        patient.insurance_provider   = p.get('insurance_provider')
        patient.insurance_policy_no  = p.get('insurance_policy_no')
        patient.save()
        return redirect('patient_list')

    return render(request, 'patients/edit.html', {'patient': patient})

def patient_delete(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        patient.delete()
        return redirect('patient_list')
    return render(request, 'patients/delete.html', {'patient': patient})
