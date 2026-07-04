from django.db import models
from patients.models import Patient
from doctors.models import Doctor

# Create your models here.
class Appointment(models.Model):
    STATUS_CHOICES = [
        ('Scheduled', 'Scheduled'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
        ('No-Show', 'No-Show'),
    ]

    PRIORITY_CHOICES = [
        ('Routine', 'Routine'),
        ('Urgent', 'Urgent'),
        ('Emergency', 'Emergency'),
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments', null=True, blank=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True, related_name='appointments')
    
    medical_record_number = models.CharField(max_length=50, blank=True, null=True, help_text="MRN - International standard patient ID")
    
    appointment_date = models.DateTimeField()
    priority_level = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='Routine')
    reason_for_visit = models.TextField(blank=True, null=True)
    allergies = models.TextField(blank=True, null=True, help_text="Any known allergies or existing medical conditions")
    insurance_provider = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Scheduled')

    def __str__(self):
        return f"{self.patient.name if self.patient else 'Unknown Patient'} - {self.appointment_date}"