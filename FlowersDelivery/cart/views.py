from django.shortcuts import render
from .models import CartItem

def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart/cart.html', {'cart_items': cart_items, 'total_price': total_price})
