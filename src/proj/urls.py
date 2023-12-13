from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from catalog.views import SearchResultView

urlpatterns = [
    path("s-admin/", admin.site.urls),
    path("references/", include("references.urls", namespace="references")),
    path("product_card/", include("product_card.urls", namespace="product_card")),
    path("", include("home_page.urls", namespace="home_page")),
    path("catalog/", include("catalog.urls", namespace="catalog")),
    path("search/", SearchResultView.as_view(), name="search_results"),
    path("carts/", include("carts.urls", namespace="carts")),
    path("order/", include("order.urls", namespace="order")),
    path("profile/", include("app_profiles.urls", namespace="profile")),
    path("admin_portal/", include("admin_portal.urls", namespace="admin_portal")),
    path("social-auth/", include("social_django.urls", namespace="social")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
