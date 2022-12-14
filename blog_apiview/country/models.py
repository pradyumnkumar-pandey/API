from django.db import models

# Create your models here.

class Country(models.Model):
    name=models.CharField(max_length=25)
    
    def __str__(self):
        return self.name

class State(models.Model):
    country=models.ForeignKey(Country,on_delete=models.CASCADE,related_name='country')
    name=models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

class City(models.Model):
    state=models.ForeignKey(State,on_delete=models.CASCADE,related_name="state")
    name=models.CharField(max_length=30)
    
    def __str__(self):
        return self.name