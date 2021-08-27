from django.db import models
from mirage import fields
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



class slot(models.Model):
    name=models.CharField(max_length=50)
    skills=models.CharField(max_length=50)
    date=models.CharField(max_length=50)
    day=models.CharField(max_length=50)
    from1=models.FloatField(max_length=20)
    to=models.FloatField(max_length=20)
    def __str__(self):
        return self.name
