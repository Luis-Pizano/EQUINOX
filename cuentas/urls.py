from django.urls import path
from . import views

urlpatterns = [
    path('registrarse/', views.registrarse, name='registrarse'),
    path('login/', views.iniciar_sesion, name='login'),
    path('logout/', views.logout, name='logout'),
]
