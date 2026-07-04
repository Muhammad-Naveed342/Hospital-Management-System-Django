from django.db import models

class Doctor(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('On Leave', 'On Leave'),
        ('Inactive', 'Inactive'),
    ]

    # Personal Info
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    nationality = models.CharField(max_length=50, blank=True, null=True)

    # Professional Info
    specialization = models.CharField(max_length=100)
    department = models.CharField(max_length=100, blank=True, null=True)
    qualification = models.CharField(max_length=200, blank=True, null=True, help_text="e.g. MBBS, MD, FRCS")
    license_number = models.CharField(max_length=50, blank=True, null=True, help_text="Medical Council License No.")
    experience_years = models.PositiveIntegerField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Active')

    # Contact Info
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    office_extension = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    # Medical Bio
    bio = models.TextField(blank=True, null=True, help_text="Short professional biography")

    def __str__(self):
        return f"Dr. {self.name} - {self.specialization}"