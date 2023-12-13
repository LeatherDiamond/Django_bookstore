from django.urls import path

from . import views

app_name = "app_profiles"
urlpatterns = [
    path("profile_view", views.ProfileView.as_view(), name="profile_view"),
    path("cancel_order/<int:pk>", views.CancelOrderView.as_view(), name="cancel_order"),
    path("order_contact_info/<int:pk>", views.ContactInfoView.as_view(), name="order_contact_info"),
]
