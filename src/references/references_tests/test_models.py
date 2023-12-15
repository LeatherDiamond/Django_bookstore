import os

import django
from django.db.utils import DataError

from dotenv import load_dotenv

import pytest

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "proj.settings")
django.setup()

load_dotenv()

from references.models import BookAuthor, BookGenre, BookPublishingHouse, BookSeries


@pytest.mark.django_db
def test_author_fields():
    author = BookAuthor.objects.create(name="John", surname="Doe")
    assert author.name == "John"
    assert author.surname == "Doe"
    assert author.description is None


@pytest.mark.django_db
def test_author_absolute_url():
    author = BookAuthor.objects.create(name="John", surname="Doe")
    assert author.get_absolute_url() == f"/references/author_preview/{author.pk}/"


@pytest.mark.django_db
def test_author_str_method():
    author = BookAuthor.objects.create(name="John", surname="Doe")
    assert str(author) == "John Doe"


@pytest.mark.django_db
def test_author_max_length():
    author = BookAuthor.objects.create(
        name="John" + "a" * 24,
        surname="Doe" + "b" * 24,
    )
    assert author.name == "John" + "a" * 24
    assert author.surname == "Doe" + "b" * 24

    with pytest.raises(DataError):
        BookAuthor.objects.create(
            name="X" * 31,
            surname="Y" * 31,
        )


@pytest.mark.django_db
def test_series_fields():
    series = BookSeries.objects.create(book_series="Harry Potter")
    assert series.book_series == "Harry Potter"
    assert series.description is None


@pytest.mark.django_db
def test_series_absolute_url():
    series = BookSeries.objects.create(book_series="Harry Potter")
    assert series.get_absolute_url() == f"/references/series_preview/{series.pk}/"


@pytest.mark.django_db
def test_series_str_method():
    series = BookSeries.objects.create(book_series="Harry Potter")
    assert str(series) == "Harry Potter"


@pytest.mark.django_db
def test_series_max_length():
    series = BookSeries.objects.create(
        book_series="Test" + "a" * 24,
    )
    assert series.book_series == "Test" + "a" * 24

    with pytest.raises(DataError):
        BookSeries.objects.create(
            book_series="X" * 31,
        )


@pytest.mark.django_db
def test_genre_fields():
    genre = BookGenre.objects.create(genre_name="Horror")
    assert genre.genre_name == "Horror"
    assert genre.description is None


@pytest.mark.django_db
def test_genre_absolute_url():
    genre = BookGenre.objects.create(genre_name="Horror")
    assert genre.get_absolute_url() == f"/references/genre_preview/{genre.pk}/"


@pytest.mark.django_db
def test_genre_str_method():
    genre = BookGenre.objects.create(
        genre_name="Horror",
    )
    assert str(genre) == "Horror"


@pytest.mark.django_db
def test_genre_max_length():
    genre = BookGenre.objects.create(
        genre_name="Test" + "a" * 24,
    )
    assert genre.genre_name == "Test" + "a" * 24

    with pytest.raises(DataError):
        BookGenre.objects.create(
            genre_name="X" * 31,
        )


@pytest.mark.django_db
def test_publisher_fields():
    publisher = BookPublishingHouse.objects.create(house_name="Penguin")
    assert publisher.house_name == "Penguin"
    assert publisher.description is None


@pytest.mark.django_db
def test_publisher_absolute_url():
    publisher = BookPublishingHouse.objects.create(house_name="Penguin")
    assert publisher.get_absolute_url() == f"/references/house_preview/{publisher.pk}/"


@pytest.mark.django_db
def test_publisher_str_method():
    publisher = BookPublishingHouse.objects.create(house_name="Penguin")
    assert str(publisher) == "Penguin"


@pytest.mark.django_db
def test_publisher_max_length():
    publisher = BookPublishingHouse.objects.create(
        house_name="Test" + "a" * 24,
    )
    assert publisher.house_name == "Test" + "a" * 24

    with pytest.raises(DataError):
        BookPublishingHouse.objects.create(
            house_name="X" * 31,
        )
