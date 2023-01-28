from django.db import models
from core.models import AbstractTimeStampedModel


class Cart(AbstractTimeStampedModel):
    cart_id = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.cart_id


class CartItem(AbstractTimeStampedModel):
    user = models.ForeignKey("users.User", related_name="cart_items", on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE, related_name="cart_items")
    variations = models.ManyToManyField("products.Variation", related_name="cart_items")
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart_items", blank=True, null=True)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.product} - {self.user}"
