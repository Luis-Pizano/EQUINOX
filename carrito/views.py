from django.shortcuts import render, redirect
from ejemplares.models import Ejemplares
from .models import Cart, CartItem
from django.http import Http404
from django.contrib import messages

# Función para formatear precios con separadores de miles
def format_price(value):
    return f"{value:,.0f}".replace(",", ".")

# Obtener el ID del carrito desde la sesión
def cart_id(request):
    try:
        cart = request.session.session_key
        if not cart:
            cart = request.session.create()
        return cart
    except Exception as e:
        print(e)

# Añadir un ejemplar al carrito
def add_cart(request, ejemplar_id):
    ejemplar = Ejemplares.objects.get(id_ejemplar=ejemplar_id)

    try:
        cart = Cart.objects.get(cart_id=cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=cart_id(request))
    cart.save()
    
    # Verificar si el ejemplar ya está en el carrito
    try:
        cart_item = CartItem.objects.get(ejemplar=ejemplar, cart=cart)
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            ejemplar=ejemplar,
            cart=cart
        )
        cart_item.save()

    return redirect('cart')

# Mostrar el carrito
def cart(request, total=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += cart_item.ejemplar.precio
    except Cart.DoesNotExist:
        cart_items = []
        total = 0

    # Calcular IVA y subtotal
    iva = total * 0.19
    subtotal = total - iva

    # Aplicar el formato a los valores (redondeando primero)
    formatted_total = format_price(total)
    formatted_iva = format_price(iva)
    formatted_subtotal = format_price(subtotal)

    context = {
        'total': formatted_total,
        'IVA': formatted_iva ,
        'subtotal': formatted_subtotal,
        'cart_items': cart_items,
    }

    return render(request, 'cart.html', context)

# Eliminar un ejemplar del carrito
def remove_cart_item(request, ejemplar_id):
    try:
        cart = Cart.objects.get(cart_id=cart_id(request))
        ejemplar = Ejemplares.objects.get(id_ejemplar=ejemplar_id)
        cart_item = CartItem.objects.get(ejemplar=ejemplar, cart=cart)
        cart_item.delete()
    except CartItem.DoesNotExist:
        raise Http404("Ejemplar no encontrado en el carrito")

    return redirect('cart')

# Vaciar el carrito completo
def remove_all_items(request):
    try:
        cart = Cart.objects.get(cart_id=cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart)
        cart_items.delete()
    except Cart.DoesNotExist:
        pass

    return redirect('cart')

def pagar(request):
    try:
        cart = Cart.objects.get(cart_id=cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart)
        cart_items.delete()
        messages.success(request,' Pago procesado exitosamente.')
         
    except Cart.DoesNotExist:
        pass

    return redirect('home')