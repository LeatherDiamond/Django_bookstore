import os

import django

import pytest

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "proj.settings")
django.setup()

from catalog.models import AppUser

from datetime import date, datetime

from references.models import BookAuthor, BookGenre, BookPublishingHouse, BookSeries

from product_card.models import Book

from django.test import Client
from django.contrib.auth.models import Permission


@pytest.fixture
def app_user_superuser():
    return AppUser.objects.create_user(
        username="superuser", password="superuserpass", is_superuser=True, is_staff=True, is_active=True
    )


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
        "view_book",
        "add_book",
        "change_book",
        "delete_book",
    ]

    for codename in permissions:
        permission = Permission.objects.get(codename=codename)
        user.user_permissions.add(permission)

    return user


@pytest.fixture
def app_user_client():
    return AppUser.objects.create_user(username="client", password="clientpass")


@pytest.fixture
def app_login_superuser(app_user_superuser):
    client = Client()
    client.login(username="superuser", password="superuserpass")
    return client


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


@pytest.fixture
def sample_product_card(sample_series, sample_publisher, sample_genre, sample_author):
    book = Book.objects.create(
        name="Test Book",
        price=10.0,
        series=sample_series,
        publishing_year="2022",
        pages=200,
        binding="Hardcover",
        format="A5",
        isbn="1234567890",
        weight=500,
        age_restriction=16,
        publishing_house=sample_publisher,
        available_books=100,
        activity="Yes",
        rating=4.5,
        date_of_addition=date.today(),
        modification_date=datetime.now(),
        description="New Book",
    )
    book.author.add(sample_author)
    book.genre.add(sample_genre)

    return book
