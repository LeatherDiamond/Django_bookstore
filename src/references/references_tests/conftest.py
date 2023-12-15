import os

import django

import pytest


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "proj.settings")
django.setup()

from references.models import BookAuthor, BookGenre, BookPublishingHouse, BookSeries


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
