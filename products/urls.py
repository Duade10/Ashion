from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path("<str:uuid>/", views.ProductDetail.as_view(), name="detail"),
]
