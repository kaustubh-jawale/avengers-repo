from django.contrib import admin

# Register your models here.
from .models import Candidate,Interviewer,Human_Resources,slot
admin.site.register(Candidate)
admin.site.register(Interviewer)
admin.site.register(Human_Resources)
admin.site.register(slot)