import random

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic

from product_card.models import Book

from references.models import BookAuthor

from .forms import NewUserForm


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                next_param = request.POST.get("next")
                if next_param:
                    url = next_param
                else:
                    url = "/"
                return HttpResponseRedirect(url)
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="home_page/login.html", context={"login_form": form})


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend="django.contrib.auth.backends.ModelBackend")
            group = Group.objects.get(name="Customers")
            user.groups.add(group)
            next_param = request.POST.get("next")
            if next_param:
                url = next_param
            else:
                url = "/"
            return HttpResponseRedirect(url)
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="home_page/register.html", context={"register_form": form})


class HomePage(generic.TemplateView):
    template_name = "home_page/home_page.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["new_book"] = self.get_random_book(genre=1)
        context["awesome_book"] = self.get_random_book(genre=5)
        context["history_book"] = self.get_random_book(genre=6)
        context["random_author"] = self.get_random_author()
        return context

    def get_random_book(self, genre):
        books = Book.objects.filter(genre=genre)

        if books.exists():
            return random.choice(books)
        else:
            return None

    def get_random_author(self):
        authors = BookAuthor.objects.all()

        if authors.exists():
            return random.choice(authors)
        else:
            return None


class ShippingInfo(generic.TemplateView):
    template_name = "home_page/shipping_info.html"


class AboutCompany(generic.TemplateView):
    template_name = "home_page/about_info.html"
