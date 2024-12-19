from django.urls import path
from . import views

urlpatterns = [
    path('agregar_pedigree/', views.agregar_pedigree, name='agregar_pedigree'),
    path('listar_pedigree/', views.listar_pedigree, name='listar_pedigree'),
    path('eliminar_pedigree/<int:id>', views.eliminar_pedigree, name='eliminar_pedigree'),
]

