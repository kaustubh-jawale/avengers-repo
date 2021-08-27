from django.db import models

class Interviewer(models.Model):
    id=models.AutoField(primary_key=True)
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    password2=models.CharField(max_length=50)
    gender=models.CharField(max_length=10)
    def __str__(self):
        return self.fname+" "+self.lname

class Human_Resources(models.Model):
        id = models.AutoField(primary_key=True)
        fname = models.CharField(max_length=50)
        lname = models.CharField(max_length=50)
        username = models.CharField(max_length=50)
        email = models.CharField(max_length=50)
        password = models.CharField(max_length=50)
        password2 = models.CharField(max_length=50)
        gender = models.CharField(max_length=10)

        def __str__(self):
            return self.fname + " " + self.lname

class Candidate(models.Model):
    candidate_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    skills = models.CharField(max_length=50)
    experience = models.FloatField()
    day = models.CharField(max_length=70)
    time = models.FloatField()

    def __str__(self):
        return self.name


class Emp(models.Model):
    emp_first_name = models.CharField(max_length=50, null="False")
    emp_last_name = models.CharField(max_length=50, null="False")
    emp_Email = models.EmailField(max_length=50, default="")
    emp_Skill = models.CharField(max_length=50, default="")
    emp_from_exp = models.FloatField(max_length=50, default="")
    emp_to_exp = models.FloatField(max_length=50, default="")
    emp_date = models.CharField(max_length=50, default="")
    emp_start_time = models.FloatField(max_length=50)
    emp_end_time = models.FloatField(max_length=50)


    def __str__(self):
            return self.emp_first_name + ' ' + self.emp_last_name




