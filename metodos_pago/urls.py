from django.urls import path
from . import views

urlpatterns = [
    path('agregar_metodo_pago/', views.agregar_metodo_pago, name='agregar_metodo_pago'),
    path('listar_metodos_pago/', views.listar_metodos_pago, name='listar_metodos_pago'),
    path('eliminar_metodo_pago/<int:id>', views.eliminar_metodo_pago, name='eliminar_metodo_pago'),
    path('editar_metodo_pago/<int:id>', views.editar_metodo_pago, name='editar_metodo_pago'),
]

