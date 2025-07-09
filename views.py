from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .models import Employee, Leave, Absence, Performance, Reward, Compensation, Payroll
from .forms import EmployeeForm, LeaveForm, AbsenceForm, PerformanceForm, RewardForm, CompensationForm, PayrollForm

# Authentication Views
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('employee_list')
    else:
        form = UserCreationForm()
    return render(request, 'employee/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('employee_list')
    else:
        form = AuthenticationForm()
    return render(request, 'employee/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('employee_list')

# Employee CRUD Operations (Require Login)
@login_required
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee/employee_list.html', {'employees': employees})

@login_required
def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee has been created successfully.')
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employee/employee_form.html', {'form': form, 'title': 'Create Employee'})

@login_required
def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'employee/employee_detail.html', {'employee': employee})

@login_required
def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, f'Employee "{employee.first_name} {employee.last_name}" has been updated successfully.')
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employee/employee_form.html', {'form': form, 'title': 'Update Employee'})

@login_required
def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        messages.success(request, f'Employee "{employee.first_name} {employee.last_name}" has been deleted successfully.')
        return redirect('employee_list')
    return render(request, 'employee/employee_confirm_delete.html', {'employee': employee})

# Leave Management (Require Login)
@login_required
def leave_list(request):
    leaves = Leave.objects.all()
    return render(request, 'employee/leave_list.html', {'leaves': leaves})

@login_required
def leave_create(request):
    if request.method == 'POST':
        form = LeaveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('leave_list')
    else:
        form = LeaveForm()
    return render(request, 'employee/leave_form.html', {'form': form, 'title': 'Request Leave'})

@login_required
def leave_update(request, pk):
    leave = get_object_or_404(Leave, pk=pk)
    if request.method == 'POST':
        form = LeaveForm(request.POST, instance=leave)
        if form.is_valid():
            form.save()
            messages.success(request, f'Employee has been updated successfully.')
            return redirect('leave_list')
    else:
        form = LeaveForm(instance=leave)
    return render(request, 'employee/leave_form.html', {'form': form, 'title': 'Update Leave'})

@login_required
def leave_delete(request, pk):
    leave = get_object_or_404(Leave, pk=pk)
    if request.method == 'POST':
        leave.delete()
        return redirect('leave_list')
    return render(request, 'employee/leave_confirm_delete.html', {'leave': leave})

# Absence Tracking (Require Login)
@login_required
def absence_list(request):
    absences = Absence.objects.all()
    return render(request, 'employee/absence_list.html', {'absences': absences})

@login_required
def absence_create(request):
    if request.method == 'POST':
        form = AbsenceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('absence_list')
    else:
        form = AbsenceForm()
    return render(request, 'employee/absence_form.html', {'form': form, 'title': 'Record Absence'})

@login_required
def absence_update(request, pk):
    absence = get_object_or_404(Absence, pk=pk)
    if request.method == 'POST':
        form = AbsenceForm(request.POST, instance=absence)
        if form.is_valid():
            form.save()
            return redirect('absence_list')
    else:
        form = AbsenceForm(instance=absence)
    return render(request, 'employee/absence_form.html', {'form': form, 'title': 'Update Absence'})

@login_required
def absence_delete(request, pk):
    absence = get_object_or_404(Absence, pk=pk)
    if request.method == 'POST':
        absence.delete()
        return redirect('absence_list')
    return render(request, 'employee/absence_confirm_delete.html', {'absence': absence})

# Performance Management (Require Login)
@login_required
def performance_list(request):
    performances = Performance.objects.all()
    return render(request, 'employee/performance_list.html', {'performances': performances})

@login_required
def performance_create(request):
    if request.method == 'POST':
        form = PerformanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('performance_list')
    else:
        form = PerformanceForm()
    return render(request, 'employee/performance_form.html', {'form': form, 'title': 'Add Performance Evaluation'})

@login_required
def performance_update(request, pk):
    performance = get_object_or_404(Performance, pk=pk)
    if request.method == 'POST':
        form = PerformanceForm(request.POST, instance=performance)
        if form.is_valid():
            form.save()
            return redirect('performance_list')
    else:
        form = PerformanceForm(instance=performance)
    return render(request, 'employee/performance_form.html', {'form': form, 'title': 'Update Performance Evaluation'})

@login_required
def performance_delete(request, pk):
    performance = get_object_or_404(Performance, pk=pk)
    if request.method == 'POST':
        performance.delete()
        return redirect('performance_list')
    return render(request, 'employee/performance_confirm_delete.html', {'performance': performance})

# Rewards and Compensation (Require Login)
@login_required
def reward_list(request):
    rewards = Reward.objects.all()
    return render(request, 'employee/reward_list.html', {'rewards': rewards})

@login_required
def reward_create(request):
    if request.method == 'POST':
        form = RewardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reward_list')
    else:
        form = RewardForm()
    return render(request, 'employee/reward_form.html', {'form': form, 'title': 'Add Reward'})

@login_required
def reward_update(request, pk):
    reward = get_object_or_404(Reward, pk=pk)
    if request.method == 'POST':
        form = RewardForm(request.POST, instance=reward)
        if form.is_valid():
            form.save()
            return redirect('reward_list')
    else:
        form = RewardForm(instance=reward)
    return render(request, 'employee/reward_form.html', {'form': form, 'title': 'Update Reward'})

@login_required
def reward_delete(request, pk):
    reward = get_object_or_404(Reward, pk=pk)
    if request.method == 'POST':
        reward.delete()
        return redirect('reward_list')
    return render(request, 'employee/reward_confirm_delete.html', {'reward': reward})

@login_required
def compensation_list(request):
    compensations = Compensation.objects.all()
    return render(request, 'employee/compensation_list.html', {'compensations': compensations})

@login_required
def compensation_create(request):
    if request.method == 'POST':
        form = CompensationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('compensation_list')
    else:
        form = CompensationForm()
    return render(request, 'employee/compensation_form.html', {'form': form, 'title': 'Add Compensation'})

@login_required
def compensation_update(request, pk):
    compensation = get_object_or_404(Compensation, pk=pk)
    if request.method == 'POST':
        form = CompensationForm(request.POST, instance=compensation)
        if form.is_valid():
            form.save()
            return redirect('compensation_list')
    else:
        form = CompensationForm(instance=compensation)
    return render(request, 'employee/compensation_form.html', {'form': form, 'title': 'Update Compensation'})

@login_required
def compensation_delete(request, pk):
    compensation = get_object_or_404(Compensation, pk=pk)
    if request.method == 'POST':
        compensation.delete()
        return redirect('compensation_list')
    return render(request, 'employee/compensation_confirm_delete.html', {'compensation': compensation})

# Payroll Management (Require Login)
@login_required
def payroll_list(request):
    payrolls = Payroll.objects.all()
    return render(request, 'employee/payroll_list.html', {'payrolls': payrolls})

@login_required
def payroll_create(request):
    if request.method == 'POST':
        form = PayrollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payroll_list')
    else:
        form = PayrollForm()
    return render(request, 'employee/payroll_form.html', {'form': form, 'title': 'Generate Payroll'})

@login_required
def payroll_detail(request, pk):
    payroll = get_object_or_404(Payroll, pk=pk)
    return render(request, 'employee/payroll_detail.html', {'payroll': payroll})

@login_required
def payroll_update(request, pk):
    payroll = get_object_or_404(Payroll, pk=pk)
    if request.method == 'POST':
        form = PayrollForm(request.POST, instance=payroll)
        if form.is_valid():
            form.save()
            return redirect('payroll_list')
    else:
        form = PayrollForm(instance=payroll)
    return render(request, 'employee/payroll_form.html', {'form': form, 'title': 'Update Payroll'})

@login_required
def payroll_detail(request, pk):
    payroll = get_object_or_404(Payroll, pk=pk)
    return render(request, 'employee/payroll_detail.html', {'payroll': payroll})

@login_required
def payroll_delete(request, pk):
    payroll = get_object_or_404(Payroll, pk=pk)
    if request.method == 'POST':
        payroll.delete()
        return redirect('payroll_list')
    return render(request, 'employee/payroll_confirm_delete.html', {'payroll': payroll})