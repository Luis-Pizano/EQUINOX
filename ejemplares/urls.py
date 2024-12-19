from django.urls import path
from django.conf.urls.static import static

from equinox import settings
from . import views


urlpatterns = [
    path('agregar_ejemplar/', views.agregar_ejemplar, name='agregar_ejemplar'),
    path('listar_ejemplares/', views.listar_ejemplares, name='listar_ejemplares'),
    path('eliminar_ejemplar/<int:id>', views.eliminar_ejemplar, name='eliminar_ejemplar'),
    path('editar_ejemplar/<int:id_ejemplar>', views.editar_ejemplar, name='editar_ejemplar'),
    path('presentacion_ejemplares/', views.presentacion_ejemplares, name='presentacion_ejemplares'),
    path('detalle_ejemplar/<int:id_ejemplar>', views.detalle_ejemplar, name='detalle_ejemplar'),
    path('buscador/', views.buscador, name='buscador'),
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
