from django.shortcuts import render
from django.views.generic import TemplateView
from braces.views import LoginRequiredMixin


class HomeView(TemplateView):
    template_name = 'home.html'