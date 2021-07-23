from django.db import models
from django.db.models.fields import EmailField

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

def __str__(self):
    return self.name
