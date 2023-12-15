from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse_lazy
from datetime import date

from references.models import BookAuthor, BookGenre, BookPublishingHouse, BookSeries


class Book(models.Model):
    name = models.CharField(max_length=70, verbose_name="Book name")
    image = models.ImageField(verbose_name="Book image", upload_to="uploads/%Y/%m/%d/", blank=True, null=True)
    author = models.ManyToManyField(
        BookAuthor,
    )
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Price", help_text="Currency in BYN")
    series = models.ForeignKey(BookSeries, verbose_name="Series", on_delete=models.PROTECT)
    genre = models.ManyToManyField(
        BookGenre,
    )
    publishing_year = models.CharField(max_length=11, verbose_name="Publishing year")
    pages = models.IntegerField(verbose_name="Pages")
    binding = models.CharField(max_length=30, verbose_name="Binding")
    format = models.CharField(max_length=7, verbose_name="Format")
    isbn = models.CharField(max_length=30, verbose_name="ISBN")
    weight = models.IntegerField(verbose_name="Weight", help_text="Weight in grams")
    age_restriction = models.IntegerField(verbose_name="Age restriction")
    publishing_house = models.ForeignKey(BookPublishingHouse, verbose_name="Publishing house", on_delete=models.PROTECT)
    available_books = models.IntegerField(verbose_name="Available books")
    activity = models.CharField(max_length=3, verbose_name="Avaliability")
    rating = models.DecimalField(max_digits=2, decimal_places=1, verbose_name="Rating")
    date_of_addition = models.DateField(verbose_name="Date of addition")
    modification_date = models.DateTimeField(auto_now=True, verbose_name="Modification date")

    description = models.TextField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse_lazy("product_card:pc_detail", kwargs={"pk": self.pk})

    def clean(self):
        if str(self.date_of_addition) > str(date.today()):
            raise ValidationError({"date_of_addition": "Must not be later than today!"})

    def __str__(self):
        return str(self.name)
