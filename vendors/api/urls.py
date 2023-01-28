from django.urls import path

from . import views

app_name = "vendors_api"

urlpatterns = [
    path("", views.VendorsListView.as_view(), name="list"),
]
