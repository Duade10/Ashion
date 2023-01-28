import datetime
from datetime import timedelta
from django.db import models
from core.models import AbstractTimeStampedModel
from shortuuidfield import ShortUUIDField
from django.urls import reverse
from django.utils import timezone


class Brand(AbstractTimeStampedModel):
    name = models.CharField(max_length=255)


class ProductManager(models.Manager):
    def active(self):
        return super().filter(is_active=True)


class Product(AbstractTimeStampedModel):

    KIDS = "kids"
    ADULTS = "adults"

    AGE_GROUP_CHOICES = ((KIDS, "Kids"), (ADULTS, "Adults"))

    name = models.CharField(max_length=255)
    uuid = ShortUUIDField()
    description = models.TextField()
    image = models.ImageField(upload_to="products/")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price = models.IntegerField(blank=True, null=True)
    stock = models.PositiveIntegerField()
    category = models.ManyToManyField("categories.Category", related_name="product")
    sub_category = models.ManyToManyField("categories.SubCategory", related_name="product")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    age_group = models.CharField(choices=AGE_GROUP_CHOICES, max_length=10, blank=True, null=True)
    objects = ProductManager()

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("products:detail", kwargs={"uuid": self.uuid})

    def in_stock(self):
        if self.stock > 0:
            return True
        else:
            return False

    def is_new(self):
        now = timezone.now()
        product_age = now - self.created_at
        if product_age > timedelta(days=3):
            return False
        else:
            return True

    def save(self, *args, **kwargs):
        self.name = str(self.name).upper()
        super().save(*args, **kwargs)


class Image(AbstractTimeStampedModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField()
    uuid = ShortUUIDField()

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"

    def __str__(self):
        return self.product.name


class VariationManager(models.Manager):
    def colour(self):
        return super().filter(variation_category="colour")

    def size(self):
        return super().filter(variation_category="size")


class Variation(AbstractTimeStampedModel):

    VARIATION_SIZE = "size"
    VARIATION_COLOUR = "colour"

    VARIATION_CHOICES = ((VARIATION_SIZE, "Size"), (VARIATION_COLOUR, "Colour"))

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="variation")
    variation_category = models.CharField(choices=VARIATION_CHOICES, max_length=7)
    variation_value = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    objects = VariationManager()

    class Meta:
        verbose_name = "Variation"
        verbose_name_plural = "Variations"

    def __str__(self):
        return f"{self.product.name} | {self.variation_category} => {self.variation_value}"
