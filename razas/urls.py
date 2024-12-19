from django.urls import path
from . import views

from django.conf.urls.static import static

from equinox import settings

urlpatterns = [
    path('agregar_raza/', views.agregar_raza, name='agregar_razas'),
    path('listar_raza/', views.listar_razas, name='listar_razas'),
    path('eliminar_raza/<int:id>', views.eliminar_raza, name='eliminar_raza'),
    path('presentacion_razas', views.presentacion_razas, name='presentacion_razas'),
    path('editar_raza/<int:id_raza>', views.editar_raza, name='editar_raza'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
