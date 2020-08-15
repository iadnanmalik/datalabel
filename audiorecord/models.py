from django.db import models

# Create your models here.
class AudioSentence(models.Model):
    sentence =models.CharField(max_length=100000)
    flag= models.BooleanField(default=0)
    def __str__(self):
        return self.sentence
class Audio(models.Model):
    name =models.CharField(max_length=25)
    voice= models.FileField()
    def __str__(self):
        return self.name
    