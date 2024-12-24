from django.urls import path
from . import views

urlpatterns = [
    path('agregar_tipo_empleado/', views.agregar_tipo_empleado, name='agregar_tipo_empleado'),
    path('listar_tipo_empleados/', views.listar_tipo_empleados, name='listar_tipo_empleados'),
    path('eliminar_tipo_empleado/<int:tipo_empleado_id>/', views.eliminar_tipo_empleado, name='eliminar_tipo_empleado'),
    path('editar_tipo_empleado/<int:tipo_empleado_id>/', views.editar_tipo_empleado, name='editar_tipo_empleado'),
]
