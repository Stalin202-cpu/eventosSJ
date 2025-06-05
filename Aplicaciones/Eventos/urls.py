from django.urls import path
from . import views

urlpatterns = [
    path('inicio2',views.inicio2,name='inicio2'),
    path('nuevoEvento', views.nuevoEvento),  # corregido
    path('guardarEvento', views.guardarEvento),  # corregido
    path('eliminarEvento/<id>', views.eliminarEvento),  # corregido
    path('editarEvento/<id>',views.editarEvento),
    path('procesarEdicionEventos', views.procesarEdicionEventos)
]
