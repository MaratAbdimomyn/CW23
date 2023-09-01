from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    middle_name = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'

class Cars(models.Model):
    brand = models.CharField(max_length=40)
    models_name = models.CharField(max_length=40)
    engine = models.CharField(max_length=40)

    def __str__(self):
        return self.models_name