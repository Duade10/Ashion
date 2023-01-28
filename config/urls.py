from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls", namespace="core")),
    path("categories/", include("categories.urls", namespace="categories")),
    path("api/categories/", include("categories.api.urls", namespace="categories_api")),
    path("accounts/", include("users.urls", namespace="users")),
    path("shop/", include("shop.urls", namespace="shop")),
    path("vendors/", include("vendors.urls", namespace="vendors")),
    path("api/vendors/", include("vendors.api.urls", namespace="vendors_api")),
    path("products/", include("products.urls", namespace="products")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
