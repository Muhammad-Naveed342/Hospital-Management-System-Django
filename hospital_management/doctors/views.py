from django.shortcuts import render, redirect, get_object_or_404
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
                gender=request.POST.get('gender'),
                date_of_birth=request.POST.get('date_of_birth') or None,
                nationality=request.POST.get('nationality'),
                specialization=specialization,
                department=request.POST.get('department'),
                qualification=request.POST.get('qualification'),
                license_number=request.POST.get('license_number'),
                experience_years=request.POST.get('experience_years') or None,
                status=request.POST.get('status') or 'Active',
                phone=phone,
                email=email,
                office_extension=request.POST.get('office_extension'),
                address=request.POST.get('address'),
                bio=request.POST.get('bio'),
            )
            return redirect('doctor_list')

    return render(request, 'doctors/add.html')

def doctor_update(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)

    if request.method == 'POST':
        doctor.name = request.POST.get('name')
        doctor.gender = request.POST.get('gender')
        doctor.date_of_birth = request.POST.get('date_of_birth') or None
        doctor.nationality = request.POST.get('nationality')
        doctor.specialization = request.POST.get('specialization')
        doctor.department = request.POST.get('department')
        doctor.qualification = request.POST.get('qualification')
        doctor.license_number = request.POST.get('license_number')
        doctor.experience_years = request.POST.get('experience_years') or None
        doctor.status = request.POST.get('status') or 'Active'
        doctor.phone = request.POST.get('phone')
        doctor.email = request.POST.get('email')
        doctor.office_extension = request.POST.get('office_extension')
        doctor.address = request.POST.get('address')
        doctor.bio = request.POST.get('bio')
        doctor.save()
        return redirect('doctor_list')

    return render(request, 'doctors/edit.html', {'doctor': doctor})

def doctor_delete(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        doctor.delete()
        return redirect('doctor_list')
    return render(request, 'doctors/delete_confirm.html', {'doctor': doctor})
