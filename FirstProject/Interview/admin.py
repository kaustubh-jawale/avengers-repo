from django.contrib import admin

# Register your models here.
from .models import Candidate,Emp,Interviewer,Human_Resources
admin.site.register(Emp)
admin.site.register(Candidate)
admin.site.register(Interviewer)
admin.site.register(Human_Resources)

