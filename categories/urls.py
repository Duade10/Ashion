from django.urls import path
from . import views

app_name = "categories"

urlpatterns = [
    path("", views.CategoriesListView.as_view(), name="list"),
]
