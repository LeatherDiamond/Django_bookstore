from references.forms import AuthorForm, GenreForm, PublishingHouseForm, SeriesForm


def test_author_form_valid():
    data = {
        "name": "New",
        "surname": "Author",
    }
    form = AuthorForm(data)
    assert form.is_valid()


def test_series_form_valid():
    data = {
        "book_series": "New",
    }
    form = SeriesForm(data)
    assert form.is_valid()


def test_genre_form_valid():
    data = {
        "genre_name": "New genre",
    }
    form = GenreForm(data)
    assert form.is_valid()


def test_publisher_form_valid():
    data = {
        "house_name": "New publisher",
    }
    form = PublishingHouseForm(data)
    assert form.is_valid()


def test_author_form_invalid():
    data = {
        "name": "",
        "surname": "",
    }
    form = AuthorForm(data)
    assert not form.is_valid()


def test_series_form_invalid():
    data = {
        "book_series": "",
    }
    form = SeriesForm(data)
    assert not form.is_valid()


def test_genre_form_invalid():
    data = {
        "genre_name": "",
    }
    form = GenreForm(data)
    assert not form.is_valid()


def test_publisher_form_invalid():
    data = {"house_name": ""}
    form = PublishingHouseForm(data)
    assert not form.is_valid()
