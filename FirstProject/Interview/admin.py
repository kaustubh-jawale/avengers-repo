from django.contrib import admin

# Register your models here.
<<<<<<< HEAD
from .models import Candidate

=======
from .models import Candidate,Employee
admin.site.register(Employee)
>>>>>>> 247da9ca82931d96dba4455f5b77502d592b4b39
admin.site.register(Candidate)
