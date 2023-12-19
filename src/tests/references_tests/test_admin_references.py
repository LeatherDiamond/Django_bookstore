from django.contrib import admin
from django.urls import reverse

import pytest

from references.models import BookAuthor, BookGenre, BookPublishingHouse, BookSeries


def test_admin_author_model():
    assert admin.site.is_registered(BookAuthor)


def test_admin_series_model():
    assert admin.site.is_registered(BookSeries)


def test_admin_genre_model():
    assert admin.site.is_registered(BookGenre)


def test_admin_publisher_model():
    assert admin.site.is_registered(BookPublishingHouse)


@pytest.mark.django_db
def test_admin_author_page_accessible(app_login_superuser, app_login_manager, app_login_client, app_anonymous_user):
    url = reverse("admin:references_bookauthor_changelist")
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
def test_admin_series_page_accessible(app_login_superuser, app_login_manager, app_login_client, app_anonymous_user):
    url = reverse("admin:references_bookseries_changelist")
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
def test_admin_genre_page_accessible(app_login_superuser, app_login_manager, app_login_client, app_anonymous_user):
    url = reverse("admin:references_bookgenre_changelist")
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
def test_admin_publisher_page_accessible(app_login_superuser, app_login_manager, app_login_client, app_anonymous_user):
    url = reverse("admin:references_bookpublishinghouse_changelist")
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
