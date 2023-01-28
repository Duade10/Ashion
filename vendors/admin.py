from django.contrib import admin
from . import models


@admin.register(models.Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ("store_name", "user", "contact_mail")
