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

GENDER_CHOICES = (
    ('M' , 'Male') ,
    ('F' , 'Female')
)

WEEK_CHOICES = (
    ('W1' , 'Week1') ,
    ('W2' , 'Week2'),
    ('W3' , 'Week3'),
    ('W4' , 'Week4'),
)

DAY_CHOICES = (
    ('Sunday' , 'Sunday') ,
    ('Monday' , 'Monday'),
    ('Tuesday' , 'Tuesday'),
    ('Wednesday' , 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
)

class Employee(models.Model):
    emp_first_name = models.CharField(max_length=50, null=False)
    emp_last_name = models.CharField(max_length=50, null=False)
    emp_ID = models.CharField(max_length=50, primary_key=True)
    emp_Email = models.EmailField(max_length=50, null=False)
    emp_Phone = models.CharField(max_length=50)
    emp_Gender = models.CharField(choices=GENDER_CHOICES, max_length=50)
    emp_Experience = models.CharField(max_length=50)
    emp_Skill = models.CharField(max_length=50)
    time_Week = models.CharField(choices=WEEK_CHOICES, max_length=50)
    time_Day = models.CharField(choices=DAY_CHOICES, max_length=50)
    time_Slot = models.CharField(max_length=50)


    def __str__(self):
            return self.emp_first_name + ' ' + self.emp_last_name

