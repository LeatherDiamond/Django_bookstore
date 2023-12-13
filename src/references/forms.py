from django import forms
from . import models


class AuthorForm(forms.ModelForm):
    class Meta:
        model = models.BookAuthor
        fields = ["name", "surname", "description"]


class SeriesForm(forms.ModelForm):
    class Meta:
        model = models.BookSeries
        fields = ["book_series", "description"]


class GenreForm(forms.ModelForm):
    class Meta:
        model = models.BookGenre
        fields = ["genre_name", "description"]


class PublishingHouseForm(forms.ModelForm):
    class Meta:
        model = models.BookPublishingHouse
        fields = ["house_name", "description"]
