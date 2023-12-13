from django.contrib import admin
from product_card.models import Book


class BookAdmin(admin.ModelAdmin):
    """Creating Admin interface"""

    list_display = (
        "name",
        "book_author",
        "book_genre",
        "price",
        "series",
        "publishing_house",
        "publishing_year",
        "pages",
        "binding",
        "format",
        "isbn",
        "weight",
        "age_restriction",
        "available_books",
        "activity",
        "rating",
        "date_of_addition",
        "modification_date",
    )

    def book_author(self, obj):
        """Printing models with M2M in Admin interface"""
        return ", ".join([p.name + " " + p.surname for p in obj.author.all()])

    def book_genre(self, obj):
        """Printing models with M2M in Admin interface"""
        return ", ".join([p.genre_name for p in obj.genre.all()])


admin.site.register(Book, BookAdmin)
