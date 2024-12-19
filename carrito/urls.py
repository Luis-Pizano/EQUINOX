from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('add_cart/<int:ejemplar_id>/', views.add_cart, name='add_cart'),
    path('remove_cart_item/<int:ejemplar_id>/', views.remove_cart_item, name='remove_cart_item'),
    path('remove_all_items/', views.remove_all_items, name='remove_all_items'),
    path('pagar/', views.pagar, name='pagar'),
]
