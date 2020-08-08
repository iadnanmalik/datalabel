from django.db import models

# Create your models here.
class Label(models.Model):
    name= models.CharField(max_length=25)
    def __str__(self):
        return self.name

class SentenceSemantic(models.Model):
    sentence =models.CharField(max_length=1000)
    flag= models.BooleanField(default=0)
    labels = models.CharField(max_length=25)
    username= models.CharField(max_length=25)
    def __str__(self):
        return self.sentence
