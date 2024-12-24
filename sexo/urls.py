from django.urls import path
from . import views

urlpatterns = [
    path('agregar_sexo/', views.agregar_sexo, name='agregar_sexo'),
    path('listar_sexo/', views.listar_sexo, name='listar_sexo'),
    path('eliminar_sexo/<int:id>', views.eliminar_sexo, name='eliminar_sexo'),
]

