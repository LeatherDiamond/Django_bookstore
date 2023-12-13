from django.urls import path

from . import views

app_name = "product_card"
urlpatterns = [
    path("pc_preview/<int:pk>/", views.ShowProductCard.as_view(), name="pc_detail"),
    path("pc_create/", views.CreateProductCard.as_view(), name="pc_create"),
    path("pc_update/<int:pk>/", views.UpdateProductCard.as_view(), name="pc_update"),
    path("pc_delete/<int:pk>/", views.DeleteProductCard.as_view(), name="pc_delete"),
    path("pc_list/", views.ShowProductCardList.as_view(), name="pc_list"),
]
