from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=50)
    description=models.CharField(max_length=200)
    active=models.BooleanField(default=True)

def __str__(self):
    return self.name


    #this is done as we are converting our model thing in sql query by migrating
    