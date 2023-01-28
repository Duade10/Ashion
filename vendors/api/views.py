from rest_framework import response, status, views

from vendors import models

from . import serializers


class VendorsListView(views.APIView):
    def get(self, request, *args, **kwargs):
        vendors = models.Vendor.objects.all()
        serializer = serializers.VendorSerializer(vendors, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)
