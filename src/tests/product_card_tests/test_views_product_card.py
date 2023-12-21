from django.urls import reverse

from product_card.models import Book

import pytest


@pytest.mark.django_db
def test_show_all_product_cards(app_login_manager, app_login_client, app_anonymous_user):
    url = reverse("product_card:pc_list")
    response_manager = app_login_manager.get(url)
    response_client = app_login_client.get(url)
    response_anonymous = app_anonymous_user.get(url)

    assert response_manager.status_code == 200

    assert response_client.status_code == 403

    assert response_anonymous.status_code == 302
    assert response_anonymous.url.startswith(reverse("home_page:login"))


@pytest.mark.django_db
def test_show_product_card_details(app_login_manager, app_login_client, app_anonymous_user, sample_product_card):
    url = reverse("product_card:pc_detail", args=[sample_product_card.pk])
    response_manager = app_login_manager.get(url)
    response_client = app_login_client.get(url)
    response_anonymous = app_anonymous_user.get(url)

    assert response_manager.status_code == 200

    assert response_client.status_code == 403

    assert response_anonymous.status_code == 302
    assert response_anonymous.url.startswith(reverse("home_page:login"))


@pytest.mark.django_db
def test_create_product_card(app_login_manager, app_login_client, app_anonymous_user, sample_product_card):
    url = reverse("product_card:pc_create")
    response_manager = app_login_manager.get(url)
    response_client = app_login_client.get(url)
    response_anonymous = app_anonymous_user.get(url)

    assert response_manager.status_code == 200

    assert response_client.status_code == 403

    assert response_anonymous.status_code == 302
    assert response_anonymous.url.startswith(reverse("home_page:login"))

    data = {
        "name": sample_product_card.name,
        "author": [sample_product_card.author.first().id],
        "price": sample_product_card.price,
        "series": sample_product_card.series.id,
        "genre": [sample_product_card.genre.first().id],
        "publishing_year": sample_product_card.publishing_year,
        "pages": sample_product_card.pages,
        "binding": sample_product_card.binding,
        "format": sample_product_card.format,
        "isbn": sample_product_card.isbn,
        "weight": sample_product_card.weight,
        "age_restriction": sample_product_card.age_restriction,
        "publishing_house": sample_product_card.publishing_house.id,
        "available_books": sample_product_card.available_books,
        "activity": sample_product_card.activity,
        "rating": sample_product_card.rating,
        "date_of_addition": sample_product_card.date_of_addition,
        "modification_date": sample_product_card.modification_date,
        "description": sample_product_card.description,
    }

    response_manager = app_login_manager.post(url, data)
    response_client = app_login_client.post(url, data)
    response_anonymous = app_anonymous_user.post(url, data)

    created_product_card = Book.objects.last()

    assert response_manager.status_code == 302
    assert response_manager.url == reverse("product_card:pc_detail", kwargs={"pk": created_product_card.pk})

    assert response_client.status_code == 403

    assert response_anonymous.status_code == 302
    assert response_anonymous.url.startswith(reverse("home_page:login"))


@pytest.mark.django_db
def test_update_product_card(app_login_manager, app_login_client, app_anonymous_user, sample_product_card):
    url = reverse("product_card:pc_update", args=[sample_product_card.pk])
    response_manager = app_login_manager.get(url)
    response_client = app_login_client.get(url)
    response_anonymous = app_anonymous_user.get(url)

    assert response_manager.status_code == 200

    assert response_client.status_code == 403

    assert response_anonymous.status_code == 302
    assert response_anonymous.url.startswith(reverse("home_page:login"))

    data = {
        "name": "Updated Name",
        "author": [sample_product_card.author.first().id],
        "price": sample_product_card.price,
        "series": sample_product_card.series.id,
        "genre": [sample_product_card.genre.first().id],
        "publishing_year": sample_product_card.publishing_year,
        "pages": sample_product_card.pages,
        "binding": sample_product_card.binding,
        "format": sample_product_card.format,
        "isbn": sample_product_card.isbn,
        "weight": sample_product_card.weight,
        "age_restriction": sample_product_card.age_restriction,
        "publishing_house": sample_product_card.publishing_house.id,
        "available_books": sample_product_card.available_books,
        "activity": sample_product_card.activity,
        "rating": sample_product_card.rating,
        "date_of_addition": sample_product_card.date_of_addition,
        "modification_date": sample_product_card.modification_date,
        "description": sample_product_card.description,
    }
    response_manager = app_login_manager.post(url, data)
    response_client = app_login_client.post(url, data)
    response_anonymous = app_anonymous_user.post(url, data)

    updated_product_card = Book.objects.get(pk=sample_product_card.pk)

    assert response_manager.status_code == 302
    assert response_manager.url == reverse("product_card:pc_detail", kwargs={"pk": updated_product_card.pk})
    assert updated_product_card.name == "Updated Name"

    assert response_client.status_code == 403

    assert response_anonymous.status_code == 302
    assert response_anonymous.url.startswith(reverse("home_page:login"))


@pytest.mark.django_db
def test_delete_product_card(app_login_manager, app_login_client, app_anonymous_user, sample_product_card):
    url = reverse("product_card:pc_delete", args=[sample_product_card.pk])
    response_manager = app_login_manager.get(url)
    response_client = app_login_client.get(url)
    response_anonymous = app_anonymous_user.get(url)

    assert response_manager.status_code == 200

    assert response_client.status_code == 403

    assert response_anonymous.status_code == 302
    assert response_anonymous.url.startswith(reverse("home_page:login"))

    response_manager = app_login_manager.post(url)
    response_client = app_login_client.post(url)
    response_anonymous = app_anonymous_user.post(url)

    assert response_manager.status_code == 302
    assert response_manager.url == reverse("product_card:pc_list")

    assert response_client.status_code == 403

    assert response_anonymous.status_code == 302
    assert response_anonymous.url.startswith(reverse("home_page:login"))
