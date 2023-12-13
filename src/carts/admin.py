from django.contrib import admin
from . import models


class CartAdmin(admin.ModelAdmin):
    list_display = ["pk", "customer"]


class BookInCartAdmin(admin.ModelAdmin):
    list_display = ["pk", "cart", "book", "quantity", "price", "total_price"]


admin.site.register(models.BooksInCart, BookInCartAdmin)
admin.site.register(models.Cart, CartAdmin)
