from django.urls import path
from . import views

urlpatterns = [
    path('agregar_cliente/', views.agregar_cliente, name='agregar_cliente'),
    path('listar_cliente/', views.listar_cliente, name='listar_clientes'),
    path('eliminar_cliente/<int:id>', views.eliminar_cliente, name='eliminar_cliente'),
    path('editar_cliente/<int:id>', views.editar_cliente, name='editar_cliente'),
]

