from django.contrib import admin

from . import models


class CartItemAdmin(admin.ModelAdmin):
    list_display = ["cart", "product", "quantity", "is_active"]
    list_display_links = ["cart", "product"]


admin.site.register(models.Cart)
admin.site.register(models.CartItem, CartItemAdmin)
