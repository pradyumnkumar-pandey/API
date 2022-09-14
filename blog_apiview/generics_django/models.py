from django.db import models

# Create your models here.

class Person(models.Model):
    GENDER = [("M", "Male"), ("F", "Female")]
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=1,choices=GENDER)
    phone=models.CharField(max_length=10)
    job_title=models.CharField(max_length=40)
    address=models.CharField(max_length=40)
    email=models.EmailField(max_length=60)
    created_at=models.DateTimeField(auto_now_add=True)
    