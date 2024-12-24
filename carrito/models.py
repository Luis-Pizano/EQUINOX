from django.db import models
from ejemplares.models import Ejemplares

class Cart(models.Model):
    cart_id = models.CharField(max_length=50, blank=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.cart_id)

class CartItem(models.Model):
    ejemplar = models.ForeignKey(Ejemplares, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.ejemplar} en el carrito"
