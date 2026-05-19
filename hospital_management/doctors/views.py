from django.shortcuts import render, redirect
from .models import Doctor

def doctor_list(request):
    doctors = Doctor.objects.all().order_by('-id')
    return render(request, 'doctors/list.html', {'doctors': doctors})

def doctor_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        specialization = request.POST.get('specialization')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        
        if name and specialization and phone and email:
            Doctor.objects.create(
                name=name,
                specialization=specialization,
                phone=phone,
                email=email
            )
            return redirect('doctor_list')
            
    return render(request, 'doctors/add.html')

