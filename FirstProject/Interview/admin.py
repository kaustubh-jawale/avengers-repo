from django.contrib import admin

# Register your models here.
from .models import Candidate,Employee,Interviewer,Human_Resources
admin.site.register(Employee)
admin.site.register(Candidate)
admin.site.register(Interviewer)
admin.site.register(Human_Resources)