from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=30)
    semestre =models.SmallIntegerField()
    

class Academico1(AbstractUser):
    # Add any additional fields here

    def __str__(self):
        return self.username