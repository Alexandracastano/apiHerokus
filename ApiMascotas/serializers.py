from asyncore import read
from dataclasses import field, fields
from pyexpat import model
from rest_framework import serializers

from .models import Mascotas

class MascotasSerializer(serializers.ModelSerializer):
    class Meta:
        model= Mascotas
        fields=('responsable', 'telefono','direccion','nombre','edad','raza','genero','color','situacion')
        