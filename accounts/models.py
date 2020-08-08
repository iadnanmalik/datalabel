from django.db import models
from django.contrib.auth.models import User
# Create your models here.
    
class Account(models.Model):
    fullName=models.CharField(max_length=25,default="none")
    gender= models.CharField(max_length=25, default="none")
    email=models.EmailField(max_length=254,default="none@example.com")
    
    def __str__(self):
        return self.fullName
