from rest_framework import serializers
from carts import models


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cart
        fields = "__all__"


class CartItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.CartItem
        fields = "__all__"
