from django.urls import path
from . import views

app_name = "carts"
urlpatterns = [
    path("update_cart/", views.CartUpdate.as_view(), name="cart_update"),
    path("delete_good_in_cart/<int:pk>", views.DeleteGoodInCartView.as_view(), name="delete_good_in_cart"),
    path("", views.CartView.as_view(), name="cart_edit"),
]
