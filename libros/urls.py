from django.urls import path
from . import views

app_name = 'libros'

urlpatterns = [
    path('listado/', views.LibroListView.as_view(), name='listado-libros'),
    path('crear/', views.LibroCreateView.as_view(), name='crear-libro'),
    path('actualizar/<int:pk>/', views.LibroUpdateView.as_view(), name='actualizar-libro'),
    path('detalle/<int:pk>/', views.LibroDetailView.as_view(), name='detalle-libro'),
]