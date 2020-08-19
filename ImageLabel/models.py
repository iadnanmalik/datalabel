from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.
class Label(models.Model):
    name= models.CharField(max_length=25)
    def __str__(self):
        return self.name

class Image(models.Model):
    flag= models.BooleanField(default=False, blank=True)
    username= models.CharField(max_length=25,blank=True)
    image=models.ImageField(upload_to='images/')
    
