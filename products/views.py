from django.shortcuts import render
from django.views import View

from . import models


class ProductDetail(View):
    def get(self, request, uuid, *args, **kwargs):
        product = models.Product.objects.get(uuid=uuid)
        context = {"product": product}
        return render(request, "products/product_detail.html", context)
