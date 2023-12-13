from django.contrib import admin
from . import models


admin.site.register(models.BookAuthor)
admin.site.register(models.BookSeries)
admin.site.register(models.BookGenre)
admin.site.register(models.BookPublishingHouse)
