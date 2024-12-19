from django.urls import path
from . import views

urlpatterns = [
    path('agregar_proveedor/', views.agregar_proveedor, name='agregar_proveedor'),
    path('listar_proveedor/', views.listar_proveedor, name='listar_proveedores'),
    path('eliminar_proveedor/<int:id>', views.eliminar_proveedor, name='eliminar_proveedor'),
    path('editar_proveedor/<int:id>/', views.editar_proveedor, name='editar_proveedor'),
]

