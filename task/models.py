from django.db import models


# Create your models here.

class courses(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField(auto_now=False, auto_now_add=False,)
    seats_available = models.IntegerField(null=True)
    slot= models.TimeField(auto_now=False, auto_now_add=False,)
    photo= models.ImageField(null=True,blank=True,upload_to = "images/")
