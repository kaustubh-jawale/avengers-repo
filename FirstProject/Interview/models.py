from django.db import models


class Candidate(models.Model):
    candidate_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    skills= models.CharField(max_length=50)
    experience = models.CharField(max_length=70)
    day = models.CharField(max_length=70)
    time = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Employee(models.Model):
    emp_first_name = models.CharField(max_length=50, null="False")
    emp_last_name = models.CharField(max_length=50, null="False")
    emp_Email = models.EmailField(max_length=50, default="")
    emp_Skill = models.CharField(max_length=50, default="")
    emp_from_exp = models.CharField(max_length=50, default="")
    emp_to_exp = models.CharField(max_length=50, default="")
    emp_date = models.CharField(max_length=50, default="")
    emp_start_time = models.CharField(max_length=50)
    emp_end_time = models.CharField(max_length=50)


    def __str__(self):
            return self.emp_first_name + ' ' + self.emp_last_name
