from django.shortcuts import render
from django.views import generic, View
from product_card.models import Book
from django.core.paginator import Paginator
from .forms import CommentForm
from django.shortcuts import get_object_or_404, render
from .models import Comment
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q


class SearchResultView(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get("q")
        results = ""
        if query:
            results = Book.objects.filter(
                Q(author__name__icontains=query)
                | Q(name__icontains=query)
                | Q(author__surname__icontains=query)
                | Q(genre__genre_name__icontains=query)
                | Q(series__book_series__icontains=query)
            ).distinct()
        paginator = Paginator(results, 12)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        return render(
            request,
            "catalog/search.html",
            context={
                "title": "Search",
                "results": page_obj,
                "count": paginator.count,
            },
        )


class CatalogView(View):
    def get(self, request, *args, **kwargs):
        book = Book.objects.all()
        paginator = Paginator(book, 12)

        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        return render(request, "catalog/catalog.html", context={"page_obj": page_obj})


class BookDetail(generic.DetailView):
    def get(self, request, *args, **kwargs):
        book = get_object_or_404(Book, pk=kwargs["pk"])
        last_posts = Book.objects.all().order_by("-id")[:3]
        comment_form = CommentForm()
        return render(
            request,
            "catalog/book_detail.html",
            context={
                "book": book,
                "last_posts": last_posts,
                "comment_form": comment_form,
            },
        )

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            text = request.POST["text"]
            username = self.request.user
            book = get_object_or_404(Book, pk=kwargs["pk"])
            comment = Comment.objects.create(book=book, username=username, text=text)
            return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))
        return render(request, "catalog/book_detail.html", context={"comment_form": comment_form})


class GenreGroup(View):
    def get(self, request, *args, **kwargs):
        genre_horror = Book.objects.filter(genre=1)
        genre_fantasy = Book.objects.filter(genre=3)
        genre_detective = Book.objects.filter(genre=4)
        genre_romance = Book.objects.filter(genre=5)
        genre_historical = Book.objects.filter(genre=6)
        return render(
            request,
            "catalog/genre_group.html",
            context={
                "genre_horror": genre_horror,
                "genre_fantasy": genre_fantasy,
                "genre_detective": genre_detective,
                "genre_romance": genre_romance,
                "genre_historical": genre_historical,
            },
        )
