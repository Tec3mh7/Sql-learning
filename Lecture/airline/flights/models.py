from django.db import models

# Create your models here.

class Fligh(models.Model):
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_lenght=64)
    duration = models.IntegerField()