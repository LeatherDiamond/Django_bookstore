from django.urls import reverse

import pytest

from references.models import BookAuthor, BookGenre, BookPublishingHouse, BookSeries


@pytest.mark.django_db
def test_show_all_authors(app_login_manager, app_login_client, app_anonymous_user):
    url = reverse("references:authors_list")
    response_manager = app_login_manager.get(url)
    response_client = app_login_client.get(url)
    response_anonymous = app_anonymous_user.get(url)

    assert response_manager.status_code == 200

    assert response_client.status_code == 403

    assert response_anonymous.status_code == 302
    assert response_anonymous.url.startswith(reverse("home_page:login"))


@pytest.mark.django_db
def test_show_author_details(app_login_manager, app_login_client, app_anonymous_user, sample_author):
    url = reverse("references:author_detail", args=[sample_author.pk])
    response_manager = app_login_manager.get(url)
    response_client = app_login_client.get(url)
    response_anonymous = app_anonymous_user.get(url)

    assert response_manager.status_code == 200

    assert response_client.status_code == 403

    assert response_anonymous.status_code == 302
    assert response_anonymous.url.startswith(reverse("home_page:login"))


@pytest.mark.django_db
def test_create_author(app_login_manager, app_login_client, app_anonymous_user):
    url = reverse("references:author_create")
    response_manager = app_login_manager.get(url)
    response_client = app_login_client.get(url)
    response_anonymous = app_anonymous_user.get(url)

    assert response_manager.status_code == 200

    assert response_client.status_code == 403

    assert response_anonymous.status_code == 302
    assert response_anonymous.url.startswith(reverse("home_page:login"))

    data = {"name": "New", "surname": "Test"}
    response_manager = app_login_manager.post(url, data)
    response_client = app_login_client.post(url, data)
    response_anonymous = app_anonymous_user.post(url, data)

    created_author = BookAuthor.objects.last()

    assert response_manager.status_code == 302
    assert response_manager.url == reverse("references:author_detail", kwargs={"pk": created_author.pk})

    assert response_client.status_code == 403

    assert response_anonymous.status_code == 302
    assert response_anonymous.url.startswith(reverse("home_page:login"))


@pytest.mark.django_db
def test_update_author(app_login_manager, app_login_client, app_anonymous_user, sample_author):
    url = reverse("references:author_update", args=[sample_author.pk])
    response_manager = app_login_manager.get(url)
    response_client = app_login_client.get(url)
    response_anonymous = app_anonymous_user.get(url)

    assert response_manager.status_code == 200

    assert response_client.status_code == 403

    assert response_anonymous.status_code == 302
    assert response_anonymous.url.startswith(reverse("home_page:login"))

    data = {
        "name": "UpdatedName",
        "surname": "UpdatedSurname",
    }
    response_manager = app_login_manager.post(url, data)
    response_client = app_login_client.post(url, data)
    response_anonymous = app_anonymous_user.post(url, data)

    updated_author = BookAuthor.objects.get(pk=sample_author.pk)

    assert response_manager.status_code == 302
    assert response_manager.url == reverse("references:author_detail", kwargs={"pk": updated_author.pk})
    assert updated_author.name == "UpdatedName"
    assert updated_author.surname == "UpdatedSurname"

    assert response_client.status_code == 403

    assert response_anonymous.status_code == 302
    assert response_anonymous.url.startswith(reverse("home_page:login"))


@pytest.mark.django_db
def test_delete_author(app_login_manager, app_login_client, app_anonymous_user, sample_author):
    url = reverse("references:author_delete", args=[sample_author.pk])
    response_manager = app_login_manager.get(url)
    response_client = app_login_client.get(url)
    response_anonymous = app_anonymous_user.get(url)

    assert response_manager.status_code == 200

    assert response_client.status_code == 403

    assert response_anonymous.status_code == 302
    assert response_anonymous.url.startswith(reverse("home_page:login"))

    response_manager = app_login_manager.post(url)
    response_client = app_login_client.post(url)
    response_anonymous = app_anonymous_user.post(url)

    assert response_manager.status_code == 302
    assert response_manager.url == reverse("references:authors_list")

    assert response_client.status_code == 403

    assert response_anonymous.status_code == 302
    assert response_anonymous.url.startswith(reverse("home_page:login"))


@pytest.mark.django_db
def test_show_all_book_series(app_login_manager, app_login_client, app_anonymous_user):
    url = reverse("references:series_list")
    response_manager = app_login_manager.get(url)
    response_client = app_login_client.get(url)
    response_anonymous = app_anonymous_user.get(url)

    assert response_manager.status_code == 200

    assert response_client.status_code == 403

    assert response_anonymous.status_code == 302
    assert response_anonymous.url.startswith(reverse("home_page:login"))


@pytest.mark.django_db
def test_show_book_series_details(app_login_manager, app_login_client, app_anonymous_user, sample_series):
    url = reverse("references:series_detail", args=[sample_series.pk])
    response_manager = app_login_manager.get(url)
    response_client = app_login_client.get(url)
    response_anonymous = app_anonymous_user.get(url)

    assert response_manager.status_code == 200

    assert response_client.status_code == 403

    assert response_anonymous.status_code == 302
    assert response_anonymous.url.startswith(reverse("home_page:login"))


@pytest.mark.django_db
def test_create_book_series(app_login_manager, app_login_client, app_anonymous_user):
    url = reverse("references:series_create")
    response_manager = app_login_manager.get(url)
    response_client = app_login_client.get(url)
    response_anonymous = app_anonymous_user.get(url)

    assert response_manager.status_code == 200

    assert response_client.status_code == 403

    assert response_anonymous.status_code == 302
    assert response_anonymous.url.startswith(reverse("home_page:login"))

    data = {
        "book_series": "New",
    }
    response_manager = app_login_manager.post(url, data)
    response_client = app_login_client.post(url, data)
    response_anonymous = app_anonymous_user.post(url, data)

    created_series = BookSeries.objects.last()

    assert response_manager.status_code == 302
    assert response_manager.url == reverse("references:series_detail", kwargs={"pk": created_series.pk})

    assert response_client.status_code == 403

    assert response_anonymous.status_code == 302
    assert response_anonymous.url.startswith(reverse("home_page:login"))


@pytest.mark.django_db
def test_update_book_series(app_login_manager, app_login_client, app_anonymous_user, sample_series):
    url = reverse("references:series_update", args=[sample_series.pk])
    response_manager = app_login_manager.get(url)
    response_client = app_login_client.get(url)
    response_anonymous = app_anonymous_user.get(url)

    assert response_manager.status_code == 200

    assert response_client.status_code == 403

    assert response_anonymous.status_code == 302
    assert response_anonymous.url.startswith(reverse("home_page:login"))

    data = {
        "book_series": "UpdatedName",
    }
    response_manager = app_login_manager.post(url, data)
    response_client = app_login_client.post(url, data)
    response_anonymous = app_anonymous_user.post(url, data)

    updated_series = BookSeries.objects.get(pk=sample_series.pk)

    assert response_manager.status_code == 302
    assert response_manager.url == reverse("references:series_detail", kwargs={"pk": updated_series.pk})
    assert updated_series.book_series == "UpdatedName"

    assert response_client.status_code == 403

    assert response_anonymous.status_code == 302
    assert response_anonymous.url.startswith(reverse("home_page:login"))


@pytest.mark.django_db
def test_delete_book_series(app_login_manager, app_login_client, app_anonymous_user, sample_series):
    url = reverse("references:series_delete", args=[sample_series.pk])
    response_manager = app_login_manager.get(url)
    response_client = app_login_client.get(url)
    response_anonymous = app_anonymous_user.get(url)

    assert response_manager.status_code == 200

    assert response_client.status_code == 403

    assert response_anonymous.status_code == 302
    assert response_anonymous.url.startswith(reverse("home_page:login"))

    response_manager = app_login_manager.post(url)
    response_client = app_login_client.post(url)
    response_anonymous = app_anonymous_user.post(url)

    assert response_manager.status_code == 302
    assert response_manager.url == reverse("references:series_list")

    assert response_client.status_code == 403

    assert response_anonymous.status_code == 302
    assert response_anonymous.url.startswith(reverse("home_page:login"))


@pytest.mark.django_db
def test_show_all_book_genres(app_login_manager, app_login_client, app_anonymous_user):
    url = reverse("references:genres_list")
    response_manager = app_login_manager.get(url)
    response_client = app_login_client.get(url)
    response_anonymous = app_anonymous_user.get(url)

    assert response_manager.status_code == 200

    assert response_client.status_code == 403

    assert response_anonymous.status_code == 302
    assert response_anonymous.url.startswith(reverse("home_page:login"))


@pytest.mark.django_db
def test_show_book_genre_details(app_login_manager, app_login_client, app_anonymous_user, sample_genre):
    url = reverse("references:genre_detail", args=[sample_genre.pk])
    response_manager = app_login_manager.get(url)
    response_client = app_login_client.get(url)
    response_anonymous = app_anonymous_user.get(url)

    assert response_manager.status_code == 200

    assert response_client.status_code == 403

    assert response_anonymous.status_code == 302
    assert response_anonymous.url.startswith(reverse("home_page:login"))


@pytest.mark.django_db
def test_create_book_genre(app_login_manager, app_login_client, app_anonymous_user):
    url = reverse("references:genre_create")
    response_manager = app_login_manager.get(url)
    response_client = app_login_client.get(url)
    response_anonymous = app_anonymous_user.get(url)

    assert response_manager.status_code == 200

    assert response_client.status_code == 403

    assert response_anonymous.status_code == 302
    assert response_anonymous.url.startswith(reverse("home_page:login"))

    data = {"genre_name": "New"}
    response_manager = app_login_manager.post(url, data)
    response_client = app_login_client.post(url, data)
    response_anonymous = app_anonymous_user.post(url, data)

    created_genre = BookGenre.objects.last()

    assert response_manager.status_code == 302
    assert response_manager.url == reverse("references:genre_detail", kwargs={"pk": created_genre.pk})

    assert response_client.status_code == 403

    assert response_anonymous.status_code == 302
    assert response_anonymous.url.startswith(reverse("home_page:login"))


@pytest.mark.django_db
def test_update_book_genre(app_login_manager, app_login_client, app_anonymous_user, sample_genre):
    url = reverse("references:genre_update", args=[sample_genre.pk])
    response_manager = app_login_manager.get(url)
    response_client = app_login_client.get(url)
    response_anonymous = app_anonymous_user.get(url)

    assert response_manager.status_code == 200

    assert response_client.status_code == 403

    assert response_anonymous.status_code == 302
    assert response_anonymous.url.startswith(reverse("home_page:login"))

    data = {
        "genre_name": "UpdatedName",
        "description": "Test Description",
    }
    response_manager = app_login_manager.post(url, data)
    response_client = app_login_client.post(url, data)
    response_anonymous = app_anonymous_user.post(url, data)

    updated_genre = BookGenre.objects.get(pk=sample_genre.pk)

    assert response_manager.status_code == 302
    assert response_manager.url == reverse("references:genre_detail", kwargs={"pk": updated_genre.pk})
    assert updated_genre.genre_name == "UpdatedName"
    assert updated_genre.description == "Test Description"

    assert response_client.status_code == 403

    assert response_anonymous.status_code == 302
    assert response_anonymous.url.startswith(reverse("home_page:login"))


@pytest.mark.django_db
def test_delete_book_genre(app_login_manager, app_login_client, app_anonymous_user, sample_genre):
    url = reverse("references:genre_delete", args=[sample_genre.pk])
    response_manager = app_login_manager.get(url)
    response_client = app_login_client.get(url)
    response_anonymous = app_anonymous_user.get(url)

    assert response_manager.status_code == 200

    assert response_client.status_code == 403

    assert response_anonymous.status_code == 302
    assert response_anonymous.url.startswith(reverse("home_page:login"))

    response_manager = app_login_manager.post(url)
    response_client = app_login_client.post(url)
    response_anonymous = app_anonymous_user.post(url)

    assert response_manager.status_code == 302
    assert response_manager.url == reverse("references:genres_list")

    assert response_client.status_code == 403

    assert response_anonymous.status_code == 302
    assert response_anonymous.url.startswith(reverse("home_page:login"))


@pytest.mark.django_db
def test_show_all_book_publishers(app_login_manager, app_login_client, app_anonymous_user):
    url = reverse("references:houses_list")
    response_manager = app_login_manager.get(url)
    response_client = app_login_client.get(url)
    response_anonymous = app_anonymous_user.get(url)

    assert response_manager.status_code == 200
    assert response_client.status_code == 200
    assert response_anonymous.status_code == 200


@pytest.mark.django_db
def test_show_book_publisher_details(app_login_manager, app_login_client, app_anonymous_user, sample_publisher):
    url = reverse("references:house_detail", args=[sample_publisher.pk])
    response_manager = app_login_manager.get(url)
    response_client = app_login_client.get(url)
    response_anonymous = app_anonymous_user.get(url)

    assert response_manager.status_code == 200

    assert response_client.status_code == 403

    assert response_anonymous.status_code == 302
    assert response_anonymous.url.startswith(reverse("home_page:login"))


@pytest.mark.django_db
def test_create_book_publisher(app_login_manager, app_login_client, app_anonymous_user):
    url = reverse("references:house_create")
    response_manager = app_login_manager.get(url)
    response_client = app_login_client.get(url)
    response_anonymous = app_anonymous_user.get(url)

    assert response_manager.status_code == 200

    assert response_client.status_code == 403

    assert response_anonymous.status_code == 302
    assert response_anonymous.url.startswith(reverse("home_page:login"))

    data = {
        "house_name": "New",
        "description": "NewDescription",
    }

    response_manager = app_login_manager.post(url, data)
    response_client = app_login_client.post(url, data)
    response_anonymous = app_anonymous_user.post(url, data)

    created_publisher = BookPublishingHouse.objects.last()

    assert response_manager.status_code == 302
    assert response_manager.url == reverse("references:house_detail", kwargs={"pk": created_publisher.pk})

    assert response_client.status_code == 403

    assert response_anonymous.status_code == 302
    assert response_anonymous.url.startswith(reverse("home_page:login"))


@pytest.mark.django_db
def test_update_book_publisher(app_login_manager, app_login_client, app_anonymous_user, sample_publisher):
    url = reverse("references:house_update", args=[sample_publisher.pk])
    response_manager = app_login_manager.get(url)
    response_client = app_login_client.get(url)
    response_anonymous = app_anonymous_user.get(url)

    assert response_manager.status_code == 200

    assert response_client.status_code == 403

    assert response_anonymous.status_code == 302
    assert response_anonymous.url.startswith(reverse("home_page:login"))

    data = {
        "house_name": "UpdatedName",
    }
    response_manager = app_login_manager.post(url, data)
    response_client = app_login_client.post(url, data)
    response_anonymous = app_anonymous_user.post(url, data)

    updated_publisher = BookPublishingHouse.objects.get(pk=sample_publisher.pk)

    assert response_manager.status_code == 302
    assert response_manager.url == reverse("references:house_detail", kwargs={"pk": updated_publisher.pk})
    assert updated_publisher.house_name == "UpdatedName"

    assert response_client.status_code == 403

    assert response_anonymous.status_code == 302
    assert response_anonymous.url.startswith(reverse("home_page:login"))


@pytest.mark.django_db
def test_delete_book_publisher(app_login_manager, app_login_client, app_anonymous_user, sample_publisher):
    url = reverse("references:house_delete", args=[sample_publisher.pk])
    response_manager = app_login_manager.get(url)
    response_client = app_login_client.get(url)
    response_anonymous = app_anonymous_user.get(url)

    assert response_manager.status_code == 200

    assert response_client.status_code == 403

    assert response_anonymous.status_code == 302
    assert response_anonymous.url.startswith(reverse("home_page:login"))

    response_manager = app_login_manager.post(url)
    response_client = app_login_client.post(url)
    response_anonymous = app_anonymous_user.post(url)

    assert response_manager.status_code == 302
    assert response_manager.url == reverse("references:houses_list")

    assert response_client.status_code == 403

    assert response_anonymous.status_code == 302
    assert response_anonymous.url.startswith(reverse("home_page:login"))
