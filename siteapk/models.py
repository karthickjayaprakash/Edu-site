from django.db import models

# Create your models here.
class book(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField(default=18)
    page=models.IntegerField(default=1)  
    

class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    mid_name= models.CharField(max_length=5)
    last_name = models.CharField(max_length=20)  
   
