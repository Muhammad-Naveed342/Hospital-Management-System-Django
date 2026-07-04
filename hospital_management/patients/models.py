from django.db import models

class Patient(models.Model):
    GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')]
    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-'),
    ]
    MARITAL_CHOICES = [
        ('Single', 'Single'), ('Married', 'Married'),
        ('Divorced', 'Divorced'), ('Widowed', 'Widowed'),
    ]
    STATUS_CHOICES = [
        ('Active', 'Active'), ('Discharged', 'Discharged'), ('Critical', 'Critical'),
    ]

    # ── Personal ──────────────────────────────────
    name            = models.CharField(max_length=100)
    date_of_birth   = models.DateField(blank=True, null=True)
    age             = models.IntegerField()
    gender          = models.CharField(max_length=10, choices=GENDER_CHOICES)
    blood_group     = models.CharField(max_length=5, choices=BLOOD_GROUP_CHOICES, blank=True, null=True)
    marital_status  = models.CharField(max_length=20, choices=MARITAL_CHOICES, blank=True, null=True)
    nationality     = models.CharField(max_length=50, blank=True, null=True)
    occupation      = models.CharField(max_length=100, blank=True, null=True)
    patient_id      = models.CharField(max_length=30, blank=True, null=True, unique=True,
                                       help_text="Hospital-assigned Patient ID e.g. PID-2024-001")

    # ── Contact ───────────────────────────────────
    phone           = models.CharField(max_length=20)
    email           = models.EmailField(blank=True, null=True)
    address         = models.TextField()

    # ── Emergency Contact ─────────────────────────
    emergency_contact_name  = models.CharField(max_length=100, blank=True, null=True)
    emergency_contact_phone = models.CharField(max_length=20, blank=True, null=True)
    emergency_contact_relation = models.CharField(max_length=50, blank=True, null=True)

    # ── Medical ───────────────────────────────────
    allergies           = models.TextField(blank=True, null=True)
    chronic_conditions  = models.TextField(blank=True, null=True, help_text="e.g. Diabetes, Hypertension")
    current_medications = models.TextField(blank=True, null=True)
    status              = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Active')

    # ── Insurance ─────────────────────────────────
    insurance_provider  = models.CharField(max_length=100, blank=True, null=True)
    insurance_policy_no = models.CharField(max_length=50, blank=True, null=True)

    # ── Meta ──────────────────────────────────────
    registered_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
