from product_card.forms import ProductCardForm

import pytest


@pytest.mark.django_db
def test_product_card_form_valid(sample_product_card):
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
    }
    form = ProductCardForm(data)
    assert form.is_valid()


@pytest.mark.django_db
def test_product_card_form_invalid(sample_product_card):
    fields_to_exclude = [
        "name",
        "author",
        "price",
        "series",
        "genre",
        "publishing_year",
        "pages",
        "binding",
        "format",
        "isbn",
        "weight",
        "age_restriction",
        "publishing_house",
        "available_books",
        "activity",
        "rating",
        "date_of_addition",
    ]

    for field in fields_to_exclude:
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
        }
        del data[field]

        form = ProductCardForm(data)
        assert not form.is_valid()
