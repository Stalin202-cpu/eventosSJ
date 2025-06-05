from django.urls import path
from . import views

urlpatterns = [
    path('inicio',views.inicio,name='inicio'),
    path('nuevoEstadio', views.nuevoEstadio),  # corregido
    path('guardarEstadio', views.guardarEstadio),  # corregido
    path('eliminarEstadio/<id>', views.eliminarEstadio),  # corregido
    path('editarEstadio/<id>',views.editarEstadio),
    path('procesarEdicionEstadios', views.procesarEdicionEstadios)
]
