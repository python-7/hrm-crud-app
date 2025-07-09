from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    job_title = models.CharField(max_length=100, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    hire_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Leave(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='Approved')

    def __str__(self):
        return f"{self.employee.first_name} - {self.start_date} to {self.end_date}"

class Absence(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    reason = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.employee.first_name} - {self.date}"

class Performance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    evaluation_date = models.DateField(auto_now_add=True)
    rating = models.IntegerField(choices=[(1, 'Poor'), (2, 'Fair'), (3, 'Good'), (4, 'Excellent'), (5, 'Outstanding')])
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.employee.first_name} - {self.evaluation_date}"

class Reward(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    date_given = models.DateField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.employee.first_name} - {self.name}"

class Compensation(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    bonus = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    effective_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.employee.first_name} - {self.effective_date}"

class Payroll(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    pay_period_start = models.DateField()
    pay_period_end = models.DateField()
    payment_date = models.DateField()
    gross_pay = models.DecimalField(max_digits=10, decimal_places=2)
    deductions = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    net_pay = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.employee.first_name} - {self.payment_date}"