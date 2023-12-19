from django.urls import resolve, reverse

from references import views


def test_author_detail_url():
    url = reverse("references:author_detail", args=[1])
    assert resolve(url).func.view_class == views.ShowAuthor
    assert url == "/references/author_preview/1/"


def test_author_create_url():
    url = reverse("references:author_create")
    assert resolve(url).func.view_class == views.CreateAuthor
    assert url == "/references/author_create/"


def test_author_update_url():
    url = reverse("references:author_update", args=[1])
    assert resolve(url).func.view_class == views.UpdateAuthor
    assert url == "/references/author_update/1/"


def test_author_delete_url():
    url = reverse("references:author_delete", args=[1])
    assert resolve(url).func.view_class == views.DeleteAuthor
    assert url == "/references/author_delete/1/"


def test_authors_list_url():
    url = reverse("references:authors_list")
    assert resolve(url).func.view_class == views.ShowAuthors
    assert url == "/references/authors_list/"


def test_series_detail_url():
    url = reverse("references:series_detail", args=[1])
    assert resolve(url).func.view_class == views.ShowSeries
    assert url == "/references/series_preview/1/"


def test_series_create_url():
    url = reverse("references:series_create")
    assert resolve(url).func.view_class == views.CreateSeries
    assert url == "/references/series_create/"


def test_series_update_url():
    url = reverse("references:series_update", args=[1])
    assert resolve(url).func.view_class == views.UpdateSeries
    assert url == "/references/series_update/1/"


def test_series_delete_url():
    url = reverse("references:series_delete", args=[1])
    assert resolve(url).func.view_class == views.DeleteSeries
    assert url == "/references/series_delete/1/"


def test_series_list_url():
    url = reverse("references:series_list")
    assert resolve(url).func.view_class == views.ShowAllSeries
    assert url == "/references/all_series_list/"


def test_genre_detail_url():
    url = reverse("references:genre_detail", args=[1])
    assert resolve(url).func.view_class == views.ShowGenre
    assert url == "/references/genre_preview/1/"


def test_genre_create_url():
    url = reverse("references:genre_create")
    assert resolve(url).func.view_class == views.CreateGenre
    assert url == "/references/genre_create/"


def test_genre_update_url():
    url = reverse("references:genre_update", args=[1])
    assert resolve(url).func.view_class == views.UpdateGenre
    assert url == "/references/genre_update/1/"


def test_genre_delete_url():
    url = reverse("references:genre_delete", args=[1])
    assert resolve(url).func.view_class == views.DeleteGenre
    assert url == "/references/genre_delete/1/"


def test_genre_list_url():
    url = reverse("references:genres_list")
    assert resolve(url).func.view_class == views.ShowGenres
    assert url == "/references/genres_list/"


def test_house_detail_url():
    url = reverse("references:house_detail", args=[1])
    assert resolve(url).func.view_class == views.ShowHouse
    assert url == "/references/house_preview/1/"


def test_house_create_url():
    url = reverse("references:house_create")
    assert resolve(url).func.view_class == views.CreateHouse
    assert url == "/references/house_create/"


def test_house_update_url():
    url = reverse("references:house_update", args=[1])
    assert resolve(url).func.view_class == views.UpdateHouse
    assert url == "/references/house_update/1/"


def test_house_delete_url():
    url = reverse("references:house_delete", args=[1])
    assert resolve(url).func.view_class == views.DeleteHouse
    assert url == "/references/house_delete/1/"


def test_houses_list_url():
    url = reverse("references:houses_list")
    assert resolve(url).func.view_class == views.ShowHouses
    assert url == "/references/houses_list/"
