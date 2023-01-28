from django.contrib import admin
from . import models


class VariationInline(admin.TabularInline):
    model = models.Variation


class ImageInline(admin.TabularInline):
    model = models.Image


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "discounted_price", "stock", "is_active", "brand")
    list_filter = ["category", "brand", "age_group"]
    search_fields = ["name"]
    list_editable = ["price"]
    inlines = [VariationInline, ImageInline]
