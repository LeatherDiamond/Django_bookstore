import os

import django
from django.db.utils import DataError

import pytest

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "proj.settings")
django.setup()

from references.models import BookAuthor, BookGenre, BookPublishingHouse, BookSeries


@pytest.mark.django_db
def test_author_fields(sample_author):
    assert sample_author.name == "John"
    assert sample_author.surname == "Doe"
    assert sample_author.description is None


@pytest.mark.django_db
def test_author_absolute_url(sample_author):
    assert sample_author.get_absolute_url() == f"/references/author_preview/{sample_author.pk}/"


@pytest.mark.django_db
def test_author_str_method(sample_author):
    assert str(sample_author) == "John Doe"


@pytest.mark.django_db
def test_author_max_length(sample_long_name_author):
    assert sample_long_name_author.name == "John" + "a" * 24
    assert sample_long_name_author.surname == "Doe" + "b" * 24

    with pytest.raises(DataError):
        BookAuthor.objects.create(
            name="X" * 31,
            surname="Y" * 31,
        )


@pytest.mark.django_db
def test_series_fields(sample_series):
    assert sample_series.book_series == "Harry Potter"
    assert sample_series.description is None


@pytest.mark.django_db
def test_series_absolute_url(sample_series):
    assert sample_series.get_absolute_url() == f"/references/series_preview/{sample_series.pk}/"


@pytest.mark.django_db
def test_series_str_method(sample_series):
    assert str(sample_series) == "Harry Potter"


@pytest.mark.django_db
def test_series_max_length(sample_long_series_name):
    assert sample_long_series_name.book_series == "Test" + "a" * 24

    with pytest.raises(DataError):
        BookSeries.objects.create(
            book_series="X" * 31,
        )


@pytest.mark.django_db
def test_genre_fields(sample_genre):
    assert sample_genre.genre_name == "Horror"
    assert sample_genre.description is None


@pytest.mark.django_db
def test_genre_absolute_url(sample_genre):
    assert sample_genre.get_absolute_url() == f"/references/genre_preview/{sample_genre.pk}/"


@pytest.mark.django_db
def test_genre_str_method(sample_genre):
    assert str(sample_genre) == "Horror"


@pytest.mark.django_db
def test_genre_max_length(sample_long_genre_name):
    assert sample_long_genre_name.genre_name == "Test" + "a" * 24

    with pytest.raises(DataError):
        BookGenre.objects.create(
            genre_name="X" * 31,
        )


@pytest.mark.django_db
def test_publisher_fields(sample_publisher):
    assert sample_publisher.house_name == "Penguin"
    assert sample_publisher.description is None


@pytest.mark.django_db
def test_publisher_absolute_url(sample_publisher):
    assert sample_publisher.get_absolute_url() == f"/references/house_preview/{sample_publisher.pk}/"


@pytest.mark.django_db
def test_publisher_str_method(sample_publisher):
    assert str(sample_publisher) == "Penguin"


@pytest.mark.django_db
def test_publisher_max_length(sample_long_publisher_name):
    assert sample_long_publisher_name.house_name == "Test" + "a" * 24

    with pytest.raises(DataError):
        BookPublishingHouse.objects.create(
            house_name="X" * 31,
        )
