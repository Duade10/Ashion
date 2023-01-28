from django.shortcuts import render
from django.views import View

from products.models import Product


class IndexView(View):
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        context = {"products": products}
        return render(request, "core/index.html", context)
