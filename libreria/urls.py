from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('nosotros', views.nosotros, name="nosotros"),
    path('libros', views.libros, name="libros"),
    path('libros/agregar', views.agregar, name="agregar"),
    path('libros/editar/<int:id>', views.editar, name="editar"),
    path('eliminar/<int:id>', views.eliminar, name="eliminar"),
]

