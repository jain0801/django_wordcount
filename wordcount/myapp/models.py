from django.db import models

# Create your models here.
class Word(models.Model):
    wordcount=models.TextField()