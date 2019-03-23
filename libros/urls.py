from django.urls import path
from . import views

app_name = 'libros'

urlpatterns = [
    path('listado/', views.LibroListView.as_view(), name='listado-libros'),
    path('detalle/<int:pk>', views.LibroDetailView.as_view(), name='detalle-libro'),
]


