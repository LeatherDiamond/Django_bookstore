from django.db import models
from django.urls import reverse_lazy


class BookAuthor(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name="Author's name",
    )
    surname = models.CharField(
        max_length=30,
        verbose_name="Author's surname",
    )
    description = models.TextField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse_lazy("references:author_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name + " " + self.surname


class BookSeries(models.Model):
    book_series = models.CharField(
        max_length=30,
        verbose_name="Books in series",
    )
    description = models.TextField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse_lazy("references:series_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return str(self.book_series)


class BookGenre(models.Model):
    genre_name = models.CharField(max_length=30, verbose_name="Genre")
    description = models.TextField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse_lazy("references:genre_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.genre_name


class BookPublishingHouse(models.Model):
    house_name = models.CharField(max_length=30, verbose_name="Publishing house")
    description = models.TextField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse_lazy("references:house_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.house_name
