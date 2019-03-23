from django.shortcuts import render

from django.views.generic import ListView, DetailView

from . import models


class LibroListView(ListView):
    model = models.Libro
    template_name = 'libro/libro-listado.html'


class LibroDetailView(DetailView):
    model = models.Libro
    template_name = 'libro/libro-detalle.html'
