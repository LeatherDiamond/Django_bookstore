from django.shortcuts import render
from django.views import generic
from . import models
from product_card.models import Book
from django.urls import reverse_lazy
from django.views import View
from django.http import HttpResponseRedirect, HttpResponse


class CartUpdate(View):
    def post(self, request):
        action = request.POST.get("submit")
        if action == "save_cart":
            cart_id = self.request.session.get("cart_id")
            cart, created = models.Cart.objects.get_or_create(
                pk=cart_id,
                defaults={},
            )
            if created:
                self.request.session["cart_id"] = cart.pk
            goods = cart.goods.all()
            if goods:
                for key, value in request.POST.items():
                    if "quantityforgood_" in key:
                        pk = int(key.split("_")[1])
                        good = goods.get(pk=pk)
                        good.quantity = int(value)
                        good.save()
            return HttpResponseRedirect(reverse_lazy("carts:cart_edit"))
        elif action == "create_order":
            return HttpResponseRedirect(reverse_lazy("order:create_order"))
        else:
            return HttpResponseRedirect(reverse_lazy("carts:cart_edit"))


class CartView(generic.DetailView):
    template_name = "carts/cart_edit.html"
    model = models.Cart

    def get_object(self, queryset=None):
        cart_id = self.request.session.get("cart_id")
        cart, created = models.Cart.objects.get_or_create(
            pk=cart_id,
            defaults={},
        )
        if created:
            self.request.session["cart_id"] = cart.pk
        book_id = self.request.GET.get("book_pk")
        if book_id:
            book = Book.objects.get(pk=int(book_id))
            book_in_cart, flat_created = models.BooksInCart.objects.update_or_create(
                cart=cart, book=book, defaults={"price": book.price}
            )
            if not flat_created:
                q = book_in_cart.quantity + 1
                book_in_cart.quantity = q
                book_in_cart.price = book_in_cart.book.price * q
            else:
                book_in_cart.price = book.price

            book_in_cart.save()
        return cart


class DeleteGoodInCartView(generic.DeleteView):
    model = models.BooksInCart
    template_name = "carts/delete_book_in_cart.html"
    success_url = reverse_lazy("carts:cart_edit")
