from django.urls import path
from . import views

urlpatterns = [
    path('registrarse/', views.registrarse, name='registrarse'),
    path('login/', views.iniciar_sesion, name='login'),
    path('logout/', views.logout, name='logout'),
    path('cuentas/', views.listar_cuentas, name='cuentas'),
    path('actualización_cuenta/<int:user_id>/', views.actualizar_cuenta, name='cuentas'),
]
