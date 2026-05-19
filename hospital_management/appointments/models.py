from django.db import models

# Create your models here.
class Appointment(models.Model):
    patient_name = models.CharField(max_length=100)
    appointment_date = models.DateTimeField()

    def __str__(self):
        return f"{self.patient_name} - {self.appointment_date}"