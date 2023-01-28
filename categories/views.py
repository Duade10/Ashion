from django.shortcuts import render
from django.views.generic import ListView
from . import models


class CategoriesListView(ListView):
    model = models.Category
    paginate_by = 10
