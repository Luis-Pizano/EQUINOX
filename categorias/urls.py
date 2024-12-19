from django.urls import path
from . import views

urlpatterns = [
    path('agregar_categoria/', views.agregar_categoria, name='agregar_categoria'),
    path('listar_categorias/', views.listar_categorias, name='listar_categorias'),
    path('eliminar_categoria/<int:id_categoria>/', views.eliminar_categoria, name='eliminar_categoria'), 
     path('editar_categoria/<int:id>/', views.editar_categoria, name='editar_categoria'),
]
