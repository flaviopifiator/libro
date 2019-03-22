from django.db import models


class Persona(models.Model):

    nombre = models.CharField(max_length=250)
    apellido = models.CharField(max_length=250)
    edad = models.PositiveIntegerField()
    dni = models.CharField(max_length=8)
    
    class Meta:
        abstract = True