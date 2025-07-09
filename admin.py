from django.contrib import admin
from .models import Employee, Leave, Absence, Performance, Reward, Compensation, Payroll

admin.site.register(Employee)
admin.site.register(Leave)
admin.site.register(Absence)
admin.site.register(Performance)
admin.site.register(Reward)
admin.site.register(Compensation)
admin.site.register(Payroll)