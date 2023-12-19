import os

import django

import pytest

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "proj.settings")
django.setup()

from catalog.models import AppUser

from references.models import BookAuthor, BookGenre, BookPublishingHouse, BookSeries

from django.test import Client
from django.contrib.auth.models import Permission


@pytest.fixture
def app_user_manager():
    user = AppUser.objects.create_user(username="manager", password="managerpass")
    permissions = [
        "view_bookauthor",
        "add_bookauthor",
        "change_bookauthor",
        "delete_bookauthor",
        "view_bookseries",
        "add_bookseries",
        "change_bookseries",
        "delete_bookseries",
        "view_bookgenre",
        "add_bookgenre",
        "change_bookgenre",
        "delete_bookgenre",
        "view_bookpublishinghouse",
        "add_bookpublishinghouse",
        "change_bookpublishinghouse",
        "delete_bookpublishinghouse",
    ]

    for codename in permissions:
        permission = Permission.objects.get(codename=codename)
        user.user_permissions.add(permission)

    return user


@pytest.fixture
def app_user_client():
    return AppUser.objects.create_user(username="client", password="clientpass")


@pytest.fixture
def app_login_manager(app_user_manager):
    client = Client()
    client.login(username="manager", password="managerpass")
    return client


@pytest.fixture
def app_login_client(app_user_client):
    client = Client()
    client.login(username="client", password="clientpass")
    return client


@pytest.fixture
def app_anonymous_user():
    return Client()


@pytest.fixture
def sample_author():
    return BookAuthor.objects.create(name="John", surname="Doe")


@pytest.fixture
def sample_long_name_author():
    return BookAuthor.objects.create(
        name="John" + "a" * 24,
        surname="Doe" + "b" * 24,
    )


@pytest.fixture
def sample_series():
    return BookSeries.objects.create(book_series="Harry Potter")


@pytest.fixture
def sample_long_series_name():
    return BookSeries.objects.create(
        book_series="Test" + "a" * 24,
    )


@pytest.fixture
def sample_genre():
    return BookGenre.objects.create(genre_name="Horror")


@pytest.fixture
def sample_long_genre_name():
    return BookGenre.objects.create(
        genre_name="Test" + "a" * 24,
    )


@pytest.fixture
def sample_publisher():
    return BookPublishingHouse.objects.create(house_name="Penguin")


@pytest.fixture
def sample_long_publisher_name():
    return BookPublishingHouse.objects.create(
        house_name="Test" + "a" * 24,
    )
