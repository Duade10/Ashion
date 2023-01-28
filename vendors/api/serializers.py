from rest_framework import serializers

from vendors import models


class VendorSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = models.Vendor
        fields = ["store_name", "contact_mail", "id", "user"]
