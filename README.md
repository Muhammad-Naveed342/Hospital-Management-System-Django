# CarePulse - Hospital Management System

A modern, responsive Hospital Management System built using Django, custom Vanilla CSS with rich glassmorphism aesthetics, and SQL database integration. It provides administrative controls to manage clinical specialists, patient records, and scheduling checkup appointments.

---

## 📂 Project Folder Structure

This workspace has been structured using industry-standard Django development patterns:

```text
E:\Hospital Management System Django\
│
├── hospital_management/               # Main Django Project Directory
│   ├── manage.py                      # Django CLI administration entry point
│   ├── db.sqlite3                     # SQLite Database holding relational tables
│   │
│   ├── hospital_management/           # Core Project Settings and Configurations
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py                # Database configurations, Static assets, Templates DIRs
│   │   ├── urls.py                    # Root URL router mapping to views
│   │   ├── views.py                   # Custom landing Dashboard metrics logic
│   │   └── wsgi.py
│   │
│   ├── patients/                      # Patients Application
│   │   ├── migrations/                # Database migration schemas
│   │   ├── admin.py                   # Patient Model Admin Registration
│   │   ├── apps.py
│   │   ├── models.py                  # Patient relational schema fields
│   │   └── views.py                   # Controller displaying list and creation views
│   │
│   ├── doctors/                       # Doctors Application
│   │   ├── migrations/
│   │   ├── admin.py                   # Doctor Model Admin Registration
│   │   ├── apps.py
│   │   ├── models.py                  # Doctor relational schema fields
│   │   └── views.py                   # Controller displaying list and creation views
│   │
│   ├── appointments/                  # Appointments Application
│   │   ├── migrations/                # Database migration schema for Appointment schedule
│   │   ├── admin.py                   # Appointment Model Admin Registration
│   │   ├── apps.py
│   │   ├── models.py                  # Appointment model mapping
│   │   └── views.py                   # Controller scheduling lists and booking views
│   │
│   ├── static/                        # Central Static Directory
│   │   └── css/
│   │       └── style.css              # Custom responsive glassmorphism theme design system
│   │
│   └── templates/                     # Central HTML Templates Directory
│       ├── base.html                  # Core Layout, Responsive Sidebar and Navbar structure
│       ├── dashboard.html             # Landing Dashboard dashboard metric charts & layouts
│       ├── patients/
│       │   ├── list.html              # Interactive Patient list table
│       │   └── add.html               # Custom Patient registration form
│       ├── doctors/
│       │   ├── list.html              # Interactive Doctor specialists listing
│       │   └── add.html               # Doctor credentials entry form
│       └── appointments/
│           ├── list.html              # Scheduled consultations list
│           └── add.html               # Appointment booking selector calendar form
│
├── myenv/                             # Python Virtual Environment isolation
├── requirements.txt                   # Automated package dependency manifest
└── README.md                          # Interactive project guide & instructions
```

---

## ⚡ Quick Start: How to Run the Project

Follow these step-by-step instructions in your terminal to initialize and boot the local server:

### 1. Open the Terminal
Open your terminal program (e.g., PowerShell, Command Prompt, or VS Code terminal) in the project workspace directory:
```powershell
# Verify you are in the workspace root
cd "E:\Hospital Management System DjanGo"
```

### 2. Activate the Virtual Environment
Activate the isolated Python virtual environment `myenv` using the corresponding shell script:

* **PowerShell (Recommended):**
  ```powershell
  .\myenv\Scripts\Activate.ps1
  ```
* **Command Prompt (CMD):**
  ```cmd
  .\myenv\Scripts\activate.bat
  ```

### 3. Install Dependencies
Install Django and required frameworks:
```powershell
pip install -r requirements.txt
```
*(Dependencies are already pre-installed inside `myenv`! Running this is just a quick confirmation checks)*

### 4. Create a Superuser (Optional but Recommended)
To access Django's built-in Admin Panel (`/admin`), create an administrator user account:
```powershell
python hospital_management/manage.py createsuperuser
```
*Follow the terminal prompts to set up your username, email, and password.*

### 5. Launch the Development Server
Start the local server in your terminal:
```powershell
python hospital_management/manage.py runserver
```

Once running successfully, copy and open the local URL in your web browser:
👉 **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**

---

## 🌟 Core Features Included

* **Live Interactive Dashboard**: Displays dynamic counters for patients, doctors, and pending appointments, with a sidebar panel for upcoming visits.
* **Specialist Directory**: View active clinical practitioners, their specialization, contact details, and register new ones.
* **Patient Registration**: Document patient information including age, gender, telephone, and residential address with client validation.
* **Consultation Booking**: Reserve appointment calendar schedules for clinical diagnostics and reviews.
* **Modern Interface**: Designed using CSS glassmorphic overlays, vibrant teal glows, Inter typography, and FontAwesome SVG branding.
