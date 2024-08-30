from django.db import models

# Create your models here.
class Student(models.Model):
    Sname = models.CharField(max_length=100)
    Branch = models.CharField(max_length=100)
    College = models.CharField(max_length=100)
    

