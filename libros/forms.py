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
    
    def __init__(self, user, *args, **kwargs):
        user = user
        super().__init__(*args, **kwargs)
        for f in self.fields:
            self.fields[f].widget.attrs['class'] = 'form-control'
        
        #mascotas_user = models.Mascota.objects.filter(user=user)
        #self.fields['mascota'].queryset = mascotas_user