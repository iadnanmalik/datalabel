from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.
class Label(models.Model):
    name= models.CharField(max_length=25)
    def __str__(self):
        return self.name

class WordSemantic(models.Model):
    sentence =models.CharField(max_length=100000)
    flag= models.BooleanField(default=0)
    labels = ArrayField(models.CharField(max_length=50), blank=True)
    username= models.CharField(max_length=25)
    def __str__(self):
        return self.sentence
