from .models import Cart, CartItem

def cart_count(request):
    cart_count = 0
    try:
        cart = Cart.objects.get(cart_id=request.session.session_key)
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        cart_count = cart_items.count()
    except Cart.DoesNotExist:
        cart_count = 0
    
    return {'cart_count': cart_count}
