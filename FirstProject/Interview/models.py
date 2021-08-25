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


