from django.urls import path
from . import views

app_name = "shop"

urlpatterns = [
    path("", views.ShopView.as_view(), name="shop"),
    path("<str:category_slug>/", views.ShopView.as_view(), name="shop_by_category"),
]
