from django.urls import path
from . import views

urlpatterns = [
    path('agregar_tipo_proveedor/', views.agregar_tipo_proveedor, name='agregar_tipo_proveedor'),
    path('listar_tipo_proveedor/', views.listar_tipo_proveedor, name='listar_tipo_proveedor'),
    path('eliminar_tipo_proveedor/<int:tipo_proveedor_id>/', views.eliminar_tipo_proveedor, name='eliminar_tipo_proveedor'),
]
