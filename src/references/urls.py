from django.urls import path

from . import views

app_name = "references"
urlpatterns = [
    path("author_preview/<int:pk>/", views.ShowAuthor.as_view(), name="author_detail"),
    path("author_create/", views.CreateAuthor.as_view(), name="author_create"),
    path("author_update/<int:pk>/", views.UpdateAuthor.as_view(), name="author_update"),
    path("author_delete/<int:pk>/", views.DeleteAuthor.as_view(), name="author_delete"),
    path("authors_list/", views.ShowAuthors.as_view(), name="authors_list"),
    path("series_preview/<int:pk>/", views.ShowSeries.as_view(), name="series_detail"),
    path("series_create/", views.CreateSeries.as_view(), name="series_create"),
    path("series_update/<int:pk>/", views.UpdateSeries.as_view(), name="series_update"),
    path("series_delete/<int:pk>/", views.DeleteSeries.as_view(), name="series_delete"),
    path("all_series_list/", views.ShowAllSeries.as_view(), name="series_list"),
    path("genre_preview/<int:pk>/", views.ShowGenre.as_view(), name="genre_detail"),
    path("genre_create/", views.CreateGenre.as_view(), name="genre_create"),
    path("genre_update/<int:pk>/", views.UpdateGenre.as_view(), name="genre_update"),
    path("genre_delete/<int:pk>/", views.DeleteGenre.as_view(), name="genre_delete"),
    path("genres_list/", views.ShowGenres.as_view(), name="genres_list"),
    path("house_preview/<int:pk>/", views.ShowHouse.as_view(), name="house_detail"),
    path("house_create/", views.CreateHouse.as_view(), name="house_create"),
    path("house_update/<int:pk>/", views.UpdateHouse.as_view(), name="house_update"),
    path("house_delete/<int:pk>/", views.DeleteHouse.as_view(), name="house_delete"),
    path("houses_list/", views.ShowHouses.as_view(), name="houses_list"),
]
