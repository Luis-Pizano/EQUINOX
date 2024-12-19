from django.urls import path
from . import views

urlpatterns = [
    path('agregar_color/', views.agregar_color, name='agregar_color'),
    path('eliminar_color/<int:id>/', views.eliminar_color, name='eliminar_color'),
    path('listar_colores/', views.listar_color, name='listar_colores'),
]

