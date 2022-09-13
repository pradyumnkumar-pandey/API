from django.db import models
# Create your models here.


class Role(models.Model):
    role_user=models.IntegerField()
    name=models.CharField(null=True,blank=True,max_length=10)
    def __str__(self):
        return self.name