from django.contrib import admin

# Register your models here.
from .models import Candidate,Employee
admin.site.register(Employee)
admin.site.register(Candidate)
