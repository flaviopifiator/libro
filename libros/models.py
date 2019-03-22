from django.db import models

from util.models import Persona


IDIOMAS = (
    ('ES', 'Español'),
    ('EN', 'Inglés'),
    ('AL', 'Alemán'),
    ('FR', 'Francés')
)


class Categoria(models.Model):
    nombre = models.CharField(max_length=250)


class Editorial(models.Model):
    nombre = models.CharField(max_length=250)
    nombre_direccion = models.CharField(max_length=250)
    numero_direccion = models.PositiveIntegerField()
 


class Autor(Persona):
    pass


class Libro(models.Model):

    titulo = models.CharField(max_length=250)
    sinopsis = models.TextField()
    precio = models.DecimalField(default=0, decimal_places=2, max_digits=4)
    idioma = models.CharField(max_length=2, choices=IDIOMAS, default='ES')
    año_publicacion = models.DateField()
    cantidad_paginas = models.PositiveIntegerField()
 
    autor = models.ManyToManyField(Autor)
    categoria = models.ManyToManyField(Categoria)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)

    def __str__(self):
        return '{} - ${}'.format(self.titulo, self.precio)


class Capitulo(models.Model):
    nombre = models.CharField(max_length=250)
    numero = models.PositiveIntegerField()

    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)