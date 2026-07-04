# CarePulse Hospital Management System

CarePulse is a modern and responsive hospital management application built with Django. It is designed to simplify the management of doctors, patients, and appointments through a clean administrative interface.

## Overview

This project provides a practical solution for handling essential hospital operations such as:

- Managing doctor records
- Registering and tracking patients
- Scheduling appointments
- Viewing a central dashboard with key information

## Features

- Dashboard with important hospital statistics
- Doctor management and record tracking
- Patient registration and profile management
- Appointment booking and scheduling
- Modern, user-friendly interface

## Technology Stack

- Python
- Django
- SQLite
- HTML, CSS, and JavaScript

## Project Structure

```text
hospital_management/
├── appointments/
├── doctors/
├── patients/
├── hospital_management/
├── static/
├── templates/
├── manage.py
├── requirements.txt
└── README.md
```

## Getting Started

### 1. Open the project folder

```powershell
cd "E:\Hospital Management System DjanGo"
```

### 2. Activate the virtual environment

```powershell
.\myenv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

### 4. Apply database migrations

```powershell
python hospital_management/manage.py migrate
```

### 5. Create a superuser (optional)

```powershell
python hospital_management/manage.py createsuperuser
```

### 6. Run the development server

```powershell
python hospital_management/manage.py runserver
```

Then open your browser and visit:

https://127.0.0.1:8000/

## Notes

This application is suitable for learning purposes, small healthcare projects, or as a base for further expansion into a full hospital management platform.
