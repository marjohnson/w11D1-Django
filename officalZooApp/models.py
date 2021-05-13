from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE

class Zoo(models.Model):
    zooName = models.CharField(max_length=45)
    zooLocation = models.CharField(max_length=255)
    zooCreateAt = models.DateTimeField(auto_now_add=True)
    zooUpdatedAt = models.DateTimeField(auto_now=True)

class Animal(models.Model):
    animalName = models.CharField(max_length=45)
    animalType = models.CharField(max_length=45)
    animalBirth = models.DateField()
    zoo = models.ForeignKey(Zoo, related_name='animals', on_delete=CASCADE)

class Employee(models.Model):
    firstName = models.CharField(max_length=45)
    lastName = models.CharField(max_length=45)
    email = models.EmailField(unique=True)
    zoo = models.ForeignKey(Zoo, related_name='employees', on_delete=CASCADE)

class Shop(models.Model):
    shopName = models.CharField(max_length=45)
    shopDescription = models.CharField(max_length=255)
    shopZoo = models.ManyToManyField(Zoo, related_name='zooShop')