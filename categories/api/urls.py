from django.urls import path
from . import views

app_name = "categories_api"

urlpatterns = [
    path("", views.CategoryListView.as_view(), name="list"),
    path("<str:cat_slug>/", views.CategoryDetailView.as_view(), name="detail"),
    path("<str:cat_slug>/sub-cat/", views.SubCategoryListView.as_view(), name="sub_cat_list"),
]
