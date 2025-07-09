from django import forms
from .models import Employee, Leave, Absence, Performance, Reward, Compensation, Payroll

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class LeaveForm(forms.ModelForm):
    class Meta:
        model = Leave
        fields = ['employee', 'start_date', 'end_date', 'reason']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

class AbsenceForm(forms.ModelForm):
    class Meta:
        model = Absence
        fields = ['employee', 'date', 'reason']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class PerformanceForm(forms.ModelForm):
    class Meta:
        model = Performance
        fields = ['employee', 'rating', 'comments']

class RewardForm(forms.ModelForm):
    class Meta:
        model = Reward
        fields = ['employee', 'name', 'description']

class CompensationForm(forms.ModelForm):
    class Meta:
        model = Compensation
        fields = ['employee', 'salary', 'bonus']

class PayrollForm(forms.ModelForm):
    class Meta:
        model = Payroll
        fields = ['employee', 'pay_period_start', 'pay_period_end', 'payment_date', 'gross_pay', 'deductions']
        widgets = {
            'pay_period_start': forms.DateInput(attrs={'type': 'date'}),
            'pay_period_end': forms.DateInput(attrs={'type': 'date'}),
            'payment_date': forms.DateInput(attrs={'type': 'date'}),
        }