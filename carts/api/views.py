from rest_framework import views, response, status
from . import serializers
from carts import models


def get_cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


class CartDataView(views.APIView):
    def get(self, request, *args, **kwargs):
        tax = 0
        total = 0
        grand_total = 0
        total_items_in_cart = 0
        user = request.user
        if user.is_authenticated:
            cart_items = models.CartItem.objects.filter(user=user, is_active=True)

        else:
            cart = models.Cart.objects.get(cart_id=get_cart_id(request))
            cart_items = models.CartItem.objects.filter(cart=cart, is_active=True)

        for cart_item in cart_items:
            total += cart_item.product.price * cart_item.quantity
            total_items_in_cart += cart_item.quantity

        if total_items_in_cart > 0:
            tax = (2 * total) / 100
            grand_total = tax + total

        data = {
            "total_items_in_cart": total_items_in_cart,
            "tax": tax,
            "grand_total": grand_total,
        }
        return response.Response(data, status=status.HTTP_200_OK)
