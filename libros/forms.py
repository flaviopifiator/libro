from django import forms

from . import models


class LibroForm(forms.ModelForm):

    class Meta:
        model = models.Libro
        fields = (
            'titulo', 'sinopsis', 'precio',
            'idioma', 'año_publicacion', 'cantidad_paginas',
            'autor', 'categoria', 'editorial',
        )