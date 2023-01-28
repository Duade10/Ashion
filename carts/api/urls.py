from django.urls import path
from . import views

app_name = "carts_api"

urlpatterns = [path("", views.CartDataView.as_view(), name="cart_data")]
