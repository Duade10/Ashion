from django.shortcuts import render
from django.views import View
from products.models import Product


class ShopView(View):
    def get(self, request, category_slug=None, *args, **kwargs):
        if category_slug is not None:
            products = Product.objects.filter(category__slug=category_slug)
        else:
            products = Product.objects.active()

        context = {"products": products}
        return render(request, "shop/shop.html", context)
