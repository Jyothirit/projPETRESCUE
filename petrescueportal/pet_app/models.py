from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=15)
    address = models.TextField()
    password = models.CharField(max_length=128)  # You might want to hash this

    def __str__(self):
        return self.username

class Rescuer(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=15)
    password = models.CharField(max_length=128)  # You might want to hash this

    def __str__(self):
        return self.username
    
    # pet_app/models.py
from django.db import models

class Pet(models.Model):
    breed = models.CharField(max_length=100)
    colour = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    identification = models.TextField()
    location = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.breed} - {self.colour}"



from django.db import models

from django.db import models

class doctor(models.Model):
    name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=15)
    password = models.CharField(max_length=128, blank=True, null=True)
    certificate = models.FileField(upload_to='certificates/',default='static/images/certimg1.jpg')

    def __str__(self):
        return self.name





