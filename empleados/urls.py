from django.urls import path
from . import views

urlpatterns = [
    path('listar_empleados/', views.listar_empleados, name='listar_empleados'),
    path('agregar/', views.agregar_empleado, name='agregar_empleado'),
    path('eliminar/<int:id>/', views.eliminar_empleado, name='eliminar_empleado'),
    path('editar_empleado/<int:id>/', views.editar_empleado, name='editar_empleado'),
]

