from distutils.command.upload import upload
from email.policy import default
from statistics import mode
from unittest.util import _MAX_LENGTH
from urllib import response
from django.db import models

# Create your models here.
class Mascotas(models.Model):
    responsable =models.CharField(max_length=60)
    telefono = models.CharField(max_length=11)
    direccion = models.CharField(max_length= 80)
    nombre = models.CharField(max_length=60)
    edad = models.PositiveIntegerField(default= 0)
    raza = models.CharField(max_length=60)
    tamaño = models.CharField(max_length=50)
    genero = models.CharField(max_length=60)
    color = models.CharField(max_length=60)
    situacion = models.CharField(max_length=200)

