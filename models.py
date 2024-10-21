from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True,max_length=150,)
    # Add more custom fields here if needed, e.g.:
    contact = models.BigIntegerField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)

class Rescuer(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    contact = models.BigIntegerField()
    password = models.CharField(max_length=128)  # You might want to hash this

    def __str__(self):
        return self.username
    


class Pet(models.Model):
    breed = models.CharField(max_length=100)
    colour = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    identification = models.TextField()
    location = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.breed} - {self.colour}"


class doctor(models.Model):
    username = models.CharField(max_length=150, unique=True)
    name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=128)
    contact = models.BigIntegerField()
    certificate = models.FileField(upload_to='certificates/',default='static/images/certimg1.jpg')
    experience = models.IntegerField()
    password = models.CharField(max_length=128)
    def _str_(self):
        return self.name
        

class Groomers(models.Model):
    name = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    email = models.EmailField()
    rate = models.CharField(max_length=15)
    location = models.CharField(max_length=150)
    certificate = models.FileField(upload_to='certificates/',default='static/images/certimg1.jpg')

    def __str__(self):
        return self.name
    
class shelters(models.Model):
    sheltername = models.CharField(max_length=100)
    email = models.EmailField()
    owner = models.CharField(max_length=55)
    phone = models.BigIntegerField()
    address = models.CharField(max_length=100)
    certificate = models.FileField(upload_to='certificates/',default='static/images/certimg1.jpg')

    def __str__(self):
        return self.name



class Message(models.Model):
    sender = models.BigIntegerField()
    sender_cat = models.IntegerField()
    recever = models.BigIntegerField()
    recever_cat = models.IntegerField()
    content = models.TextField()

    def __str__(self):
        return self.content