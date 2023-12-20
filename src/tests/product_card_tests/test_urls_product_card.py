from django.urls import resolve, reverse

from product_card import views


def test_product_card_detail_url():
    url = reverse("product_card:pc_detail", args=[1])
    assert resolve(url).func.view_class == views.ShowProductCard
    assert url == "/product_card/pc_preview/1/"


def test_product_card_create_url():
    url = reverse("product_card:pc_create")
    assert resolve(url).func.view_class == views.CreateProductCard
    assert url == "/product_card/pc_create/"


def test_product_card_update_url():
    url = reverse("product_card:pc_update", args=[1])
    assert resolve(url).func.view_class == views.UpdateProductCard
    assert url == "/product_card/pc_update/1/"


def test_product_card_delete_url():
    url = reverse("product_card:pc_delete", args=[1])
    assert resolve(url).func.view_class == views.DeleteProductCard
    assert url == "/product_card/pc_delete/1/"


def test_product_cards_list_url():
    url = reverse("product_card:pc_list")
    assert resolve(url).func.view_class == views.ShowProductCardList
    assert url == "/product_card/pc_list/"
