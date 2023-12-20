from django.contrib import admin
from django.urls import reverse

from product_card.models import Book

import pytest

from references.models import BookAuthor, BookGenre


def test_product_card_admin_model():
    assert admin.site.is_registered(Book)


@pytest.mark.django_db
def test_admin_product_card_accessible(app_login_superuser, app_login_manager, app_login_client, app_anonymous_user):
    url = reverse("admin:product_card_book_changelist")
    response_superuser = app_login_superuser.get(url)
    response_manager = app_login_manager.get(url)
    response_client = app_login_client.get(url)
    response_anonymous = app_anonymous_user.get(url)

    assert response_superuser.status_code == 200

    assert response_manager.status_code == 302
    assert response_manager.url.startswith("/s-admin/login/")

    assert response_client.status_code == 302
    assert response_client.url.startswith("/s-admin/login/")

    assert response_anonymous.status_code == 302
    assert response_anonymous.url.startswith("/s-admin/login/")


@pytest.mark.django_db
def test_book_author_method(app_login_superuser, sample_product_card):
    author1 = BookAuthor.objects.create(name="John", surname="Doe")
    author2 = BookAuthor.objects.create(name="Jane", surname="Doe")
    sample_product_card.author.add(author1, author2)

    url = reverse("admin:product_card_book_change", args=[sample_product_card.pk])
    response = app_login_superuser.get(url)

    assert all(
        author in response.content.decode("utf-8")
        for author in [f"{author1.name} {author1.surname}", f"{author2.name} {author2.surname}"]
    )


@pytest.mark.django_db
def test_book_genre_method(app_login_superuser, sample_product_card):
    genre1 = BookGenre.objects.create(genre_name="Mystery")
    genre2 = BookGenre.objects.create(genre_name="Thriller")
    sample_product_card.genre.add(genre1, genre2)

    url = reverse("admin:product_card_book_change", args=[sample_product_card.pk])
    response = app_login_superuser.get(url)

    assert all(genre in response.content.decode("utf-8") for genre in [genre1.genre_name, genre2.genre_name])
