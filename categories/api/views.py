from rest_framework import views, response, status
from categories import models
from . import serializers


class CategoryListView(views.APIView):
    def get(self, request, *args, **kwargs):
        categories = models.Category.objects.all()
        serializer = serializers.CategorySerializer(categories, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)


class CategoryDetailView(views.APIView):
    def get(self, request, cat_slug, *args, **kwargs):
        category = models.Category.objects.get(slug=cat_slug)
        serializer = serializers.CategorySerializer(category)
        return response.Response(serializer.data, status=status.HTTP_200_OK)


class SubCategoryListView(views.APIView):
    def get(self, request, cat_slug, *args, **kwargs):
        category = models.Category.objects.get(slug=cat_slug)
        subcat = models.SubCategory.objects.filter(category=category)
        serializer = serializers.SubCategorySerializer(subcat, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)
