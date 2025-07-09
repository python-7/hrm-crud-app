Human Resource Management Information System (HRMIS)
This is a web-based Human Resource Management Information System (HRMIS) built using the Django framework and styled with Tailwind CSS. It provides basic CRUD (Create, Read, Update, Delete) operations for employee management, along with dedicated portals for both administrators and employees, and features for leave management, performance reviews, attendance tracking, and payslip viewing.

Table of Contents
Features

Technologies Used

Project Structure

Setup and Installation

Prerequisites

Backend Setup

Frontend Setup (Tailwind CSS)

Database Migrations

Creating a Superuser

Usage

Admin Portal

Employee Portal

Future Enhancements

Contributing

License

Features
Employee Management (CRUD):

Add new employee records.

View detailed employee profiles.

Update existing employee information.

Delete employee records.

User Authentication & Authorization:

Secure login and logout.

Role-based access control (Admin vs. Employee).

Admin Portal:

Dashboard with key HR metrics (total employees, active employees, pending leave requests).

Centralized management of all HR functions.

Access to Django Admin for direct database management.

Employee Portal:

Personalized dashboard displaying employee's own profile.

Quick links to personal HR functions.

Leave Management:

Employees can submit leave requests (Annual, Sick, Maternity, Paternity, Unpaid, Other).

Admins can view, approve, reject, or cancel leave requests.

Notifications for leave request status changes.

Performance Reviews:

Admins can create and manage performance review records for employees.

Employees can view their own performance reviews.

Includes fields for ratings, comments, goals achieved, and areas for development.

Attendance Tracking:

Employees can clock in and clock out daily.

Records daily attendance with timestamps.

View personal attendance history.

Admins can view all attendance records.

Payslip Management:

Admins can upload/record payslip details for employees.

Employees can view their historical payslips (conceptual, links to external URL for actual PDF).

Notifications for new payslips.

Notifications System:

In-app notifications for users regarding HR actions (e.g., leave approval, new payslip).

Ability to mark notifications as read.

Responsive Design:

Built with Tailwind CSS for a modern, mobile-first, and responsive user interface.

Technologies Used
Backend:

Python 3.x

Django 5.x

Django Crispy Forms (for elegant form rendering)

Crispy Tailwind (Tailwind template pack for Crispy Forms)

Frontend:

HTML5

Tailwind CSS 3.x

Font Awesome (for icons)

Database:

SQLite (default for development, easily configurable for PostgreSQL/MySQL in production)

Project Structure
hrmis_project/
├── hrmis_project/         # Main Django project directory
│   ├── settings.py        # Project settings (Tailwind config, INSTALLED_APPS)
│   ├── urls.py            # Main URL configurations
│   └── ...
├── employees/             # Django app for HR functionalities
│   ├── migrations/        # Database migrations
│   ├── models.py          # Defines Employee, LeaveRequest, PerformanceReview, etc. models
│   ├── forms.py           # Django forms for model interaction
│   ├── views.py           # Handles business logic and renders templates
│   ├── urls.py            # App-specific URL configurations
│   ├── admin.py           # Registers models with Django Admin
│   └── ...
├── templates/             # Global templates directory
│   ├── base.html          # Base template with navbar, messages, and Tailwind setup
│   ├── registration/      # Authentication templates (login.html)
│   ├── portals/           # Dashboard templates (admin_dashboard.html, employee_dashboard.html)
│   ├── employees/         # Employee CRUD templates
│   ├── leave/             # Leave management templates
│   ├── performance/       # Performance review templates
│   ├── attendance/        # Attendance tracking templates
│   ├── payroll/           # Payslip templates
│   └── notifications/     # Notification templates
├── static/                # Compiled static assets (CSS, JS)
│   └── css/
│       └── main.css       # Compiled Tailwind CSS output
├── manage.py              # Django management utility
├── tailwind.config.js     # Tailwind CSS configuration
├── postcss.config.js      # PostCSS configuration for Tailwind
└── requirements.txt       # Python dependencies

Setup and Installation
Follow these steps to get the HRMIS project up and running on your local machine.

Prerequisites
Python 3.8+

pip (Python package installer)

Node.js and npm (Node Package Manager) - Required for Tailwind CSS compilation.

Backend Setup
Clone the repository:

git clone <repository_url>
cd hrmis_project

Create a virtual environment (recommended):

python -m venv venv
source venv/bin/activate  # On Windows: `venv\Scripts\activate`

Install Python dependencies:

pip install -r requirements.txt
# Or manually:
# pip install django djangorestframework django-crispy-forms crispy-tailwind django-tailwind

(Create a requirements.txt file in your project root with the installed packages if you don't have one.)

# requirements.txt
Django==5.x.x
django-crispy-forms==2.x.x
crispy-tailwind==1.x.x
django-tailwind==3.x.x
# Add other dependencies as you install them

Frontend Setup (Tailwind CSS)
Initialize Tailwind CSS for Django:

python manage.py tailwind init

This command will create tailwind.config.js and postcss.config.js in your project root.

Install Tailwind's Django App:

python manage.py tailwind install_app

This creates a Django app (e.g., theme) that Tailwind uses for its static files. Ensure this app is added to INSTALLED_APPS in hrmis_project/settings.py.

Configure settings.py for Tailwind and Crispy Forms:
Open hrmis_project/settings.py and ensure the following are present in INSTALLED_APPS and configured:

# hrmis_project/settings.py

INSTALLED_APPS = [
    # ... existing Django apps
    'employees',
    'tailwind',
    'theme', # Or whatever you named your tailwind app
    'crispy_forms',
    'crispy_tailwind',
]

# ... other settings

# Tailwind CSS configuration
TAILWIND_APP_NAME = 'theme' # This should match the app name you created
NPM_BIN_PATH = '/usr/local/bin/npm' # Adjust this path if npm is not found (e.g., 'npm' or full path)

# Crispy Forms configuration
CRISPY_ALLOWED_TEMPLATE_PACKS = "tailwind"
CRISPY_TEMPLATE_PACK = "tailwind"

# Static files configuration
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'), # Ensure this points to your static folder
]

# Template DIRS
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')], # Ensure this is included
        'APP_DIRS': True,
        # ...
    },
]

# Redirect after login/logout
LOGIN_REDIRECT_URL = '/employee-dashboard/'
LOGOUT_REDIRECT_URL = '/login/'

Build Tailwind CSS:
This compiles your Tailwind CSS classes into a static CSS file (static/css/main.css).

python manage.py tailwind build

For development, you can run this command in a separate terminal to watch for changes and recompile automatically:

python manage.py tailwind start

Database Migrations
Apply the database migrations to create the necessary tables for the employees app:

python manage.py makemigrations employees
python manage.py migrate

Creating a Superuser
Create a superuser account to access the Django admin panel and manage initial data:

python manage.py createsuperuser

Follow the prompts to set up your username, email, and password.

Usage
Run the Django development server:

python manage.py runserver

The application will be accessible at http://127.0.0.1:8000/.

Access Django Admin:
Navigate to http://127.0.0.1:8000/admin/ and log in with the superuser credentials you created. Here, you can manage Users, Employees, Leave Requests, Performance Reviews, Attendance, Payslips, and Notifications.

Admin Portal
Log in as a superuser or a staff user.

Access the Admin Dashboard via the navigation bar.

From the dashboard, you can navigate to:

Manage Employees: View, add, edit, and delete employee records.

Manage Leave Requests: Review and update the status of submitted leave requests.

Manage Performance Reviews: Create and view employee performance evaluations.

Manage Payslips: Upload and view payslip records.

View Attendance Records: See all employee attendance data.

Employee Portal
Ensure an Employee record is linked to a User account (this can be done in the Django Admin).

Log in with the linked user account.

Access the Employee Dashboard via the navigation bar.

From the dashboard, employees can:

View their personal profile.

Submit new leave requests and view the status of their existing requests.

View their performance reviews.

Clock in/out and view their attendance history.

View their payslips.

See their in-app notifications.

Future Enhancements
User Registration: Implement a public registration form for new users, potentially with an approval workflow for HR.

Document Management: Allow employees to upload and manage personal documents (e.g., certificates, contracts).

Payroll Integration: Integrate with a real payroll system or implement more complex payroll calculations.

Reporting & Analytics: Generate detailed reports on various HR metrics.

Notifications (Real-time): Implement real-time notifications using WebSockets (e.g., Django Channels).

Employee Self-Service: Expand options for employees to update their own profile information (with HR approval).

Mobile App: Develop a complementary mobile application.

Internationalization (i18n): Support multiple languages.

Contributing
Contributions are welcome! Please feel free to fork the repository, open issues
