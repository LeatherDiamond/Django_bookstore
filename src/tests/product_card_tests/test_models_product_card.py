from datetime import date, timedelta

from django.core.exceptions import ValidationError
from django.db.utils import DataError
from django.urls import reverse_lazy

from product_card.models import Book

import pytest


@pytest.mark.django_db
def test_create_book(sample_product_card):
    assert Book.objects.count() == 1
    assert sample_product_card.name == "Test Book"
    assert sample_product_card.get_absolute_url() == reverse_lazy(
        "product_card:pc_detail", kwargs={"pk": sample_product_card.pk}
    )


@pytest.mark.django_db
def test_str_method(sample_product_card):
    assert str(sample_product_card) == "Test Book"


@pytest.mark.django_db
def test_clean_method_valid(sample_product_card):
    assert sample_product_card.clean() is None


@pytest.mark.django_db
def test_clean_method_invalid(sample_product_card):
    sample_product_card.date_of_addition = date.today() + timedelta(days=1)
    with pytest.raises(ValidationError, match="Must not be later than today!"):
        sample_product_card.clean()


@pytest.mark.django_db
def test_name_field_max_len():
    with pytest.raises(DataError):
        Book.objects.create(
            name="X" * 72,
        )


@pytest.mark.django_db
def test_price_field_max_len():
    with pytest.raises(DataError):
        Book.objects.create(
            price=1000000,
        )


@pytest.mark.django_db
def test_publishing_year_field_max_len():
    with pytest.raises(DataError):
        Book.objects.create(
            publishing_year="202220222022202",
        )


@pytest.mark.django_db
def test_binding_field_max_len():
    with pytest.raises(DataError):
        Book.objects.create(
            binding="Hardcover" + "X" * 30,
        )


@pytest.mark.django_db
def test_format_field_max_len():
    with pytest.raises(DataError):
        Book.objects.create(
            format="A5" + "A" * 7,
        )


@pytest.mark.django_db
def test_isbn_field_max_len():
    with pytest.raises(DataError):
        Book.objects.create(
            isbn="123" + "1" * 30,
        )


@pytest.mark.django_db
def test_activity_field_max_len():
    with pytest.raises(DataError):
        Book.objects.create(
            activity="Yes" + "X" * 3,
        )


@pytest.mark.django_db
def test_rating_field_max_len():
    with pytest.raises(DataError):
        Book.objects.create(
            rating=888,
        )
