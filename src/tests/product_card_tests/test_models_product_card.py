from datetime import date, timedelta

from django.core.exceptions import ValidationError
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
