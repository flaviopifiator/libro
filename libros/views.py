from django.shortcuts import render
from django.urls import reverse_lazy
from core.views import LoginRequiredMixin

from django.views.generic import ListView, DetailView, CreateView, UpdateView

from . import models, forms


class LibroListView(LoginRequiredMixin, ListView):
    model = models.Libro
    template_name = 'libro/libro-listado.html'


class LibroDetailView(LoginRequiredMixin, DetailView):
    model = models.Libro
    template_name = 'libro/libro-detalle.html'


class LibroCreateView(LoginRequiredMixin, CreateView):
    model = models.Libro
    template_name = 'libro/libro-form.html'
    success_url = reverse_lazy('libro:listado-libros')
    form_class = forms.LibroForm


class LibroUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Libro
    template_name = 'libro/libro-form.html'
    success_url = reverse_lazy('libro:listado-libros')
    form_class = forms.LibroForm



