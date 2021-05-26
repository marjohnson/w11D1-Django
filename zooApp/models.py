from django.db import models

class Animals(models.Model):
    animalName = models.CharField(max_length=45)
    animalType = models.CharField(max_length=45)
    animalBirth = models.DateTimeField()
    animalAdded = models.DateTimeField(auto_now_add=True)
    animalUpdated = models.DateTimeField(auto_now=True)
