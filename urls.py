from django.urls import path
from . import views

urlpatterns = [
    # Authentication URLs
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    # Employee URLs
    path('employees/', views.employee_list, name='employee_list'),
    path('employees/create/', views.employee_create, name='employee_create'),
    path('employees/<int:pk>/', views.employee_detail, name='employee_detail'),
    path('employees/<int:pk>/update/', views.employee_update, name='employee_update'),
    path('employees/<int:pk>/delete/', views.employee_delete, name='employee_delete'),

    # Leave URLs
    path('leaves/', views.leave_list, name='leave_list'),
    path('leaves/create/', views.leave_create, name='leave_create'),
    path('leaves/<int:pk>/update/', views.leave_update, name='leave_update'),
    path('leaves/<int:pk>/delete/', views.leave_delete, name='leave_delete'),

    # Absence URLs
    path('absences/', views.absence_list, name='absence_list'),
    path('absences/create/', views.absence_create, name='absence_create'),
    path('absences/<int:pk>/update/', views.absence_update, name='absence_update'),
    path('absences/<int:pk>/delete/', views.absence_delete, name='absence_delete'),

    # Performance URLs
    path('performance/', views.performance_list, name='performance_list'),
    path('performance/create/', views.performance_create, name='performance_create'),
    path('performance/<int:pk>/update/', views.performance_update, name='performance_update'),
    path('performance/<int:pk>/delete/', views.performance_delete, name='performance_delete'),

    # Reward URLs
    path('rewards/', views.reward_list, name='reward_list'),
    path('rewards/create/', views.reward_create, name='reward_create'),
    path('rewards/<int:pk>/update/', views.reward_update, name='reward_update'),
    path('rewards/<int:pk>/delete/', views.reward_delete, name='reward_delete'),

    # Compensation URLs
    path('compensation/', views.compensation_list, name='compensation_list'),
    path('compensation/create/', views.compensation_create, name='compensation_create'),
    path('compensation/<int:pk>/update/', views.compensation_update, name='compensation_update'),
    path('compensation/<int:pk>/delete/', views.compensation_delete, name='compensation_delete'),

    # Payroll URLs
    path('payroll/', views.payroll_list, name='payroll_list'),
    path('payroll/create/', views.payroll_create, name='payroll_create'),
    path('payroll/<int:pk>/', views.payroll_detail, name='payroll_detail'),
    path('payroll/<int:pk>/update/', views.payroll_update, name='payroll_update'),
    path('payroll/<int:pk>/delete/', views.payroll_delete, name='payroll_delete'),
]