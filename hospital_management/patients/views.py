from django.shortcuts import render, redirect
from .models import Patient

def patient_list(request):
    patients = Patient.objects.all().order_by('-id')
    return render(request, 'patients/list.html', {'patients': patients})

def patient_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        
        if name and age and gender and address and phone:
            Patient.objects.create(
                name=name,
                age=age,
                gender=gender,
                address=address,
                phone=phone
            )
            return redirect('patient_list')
            
    return render(request, 'patients/add.html')

