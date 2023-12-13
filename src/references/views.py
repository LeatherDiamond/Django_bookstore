from . import models, forms
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class ShowAuthors(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    login_url = "home_page:login"
    permission_required = "references.view_bookauthor"
    model = models.BookAuthor
    template_name = "references/list_author.html"


class ShowAuthor(LoginRequiredMixin, PermissionRequiredMixin, generic.DetailView):
    model = models.BookAuthor
    login_url = "home_page:login"
    permission_required = "references.view_bookauthor"
    template_name = "references/detail_author.html"


class CreateAuthor(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    login_url = "home_page:login"
    permission_required = "references.add_bookauthor"
    model = models.BookAuthor
    form_class = forms.AuthorForm
    template_name = "references/edit_author.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["operation_name"] = "Create"
        return context


class UpdateAuthor(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    login_url = "home_page:login"
    permission_required = "references.change_bookauthor"
    model = models.BookAuthor
    form_class = forms.AuthorForm
    template_name = "references/edit_author.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["operation_name"] = "Update"
        return context


class DeleteAuthor(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    login_url = "home_page:login"
    permission_required = "references.delete_bookauthor"
    model = models.BookAuthor
    template_name = "references/delete_author.html"

    def get_success_url(self):
        return reverse_lazy("references:authors_list")


class ShowAllSeries(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    login_url = "home_page:login"
    permission_required = "references.view_bookseries"
    model = models.BookSeries
    template_name = "references/list_series.html"


class ShowSeries(LoginRequiredMixin, PermissionRequiredMixin, generic.DetailView):
    login_url = "home_page:login"
    permission_required = "references.view_bookseries"
    model = models.BookSeries
    template_name = "references/detail_series.html"


class CreateSeries(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    login_url = "home_page:login"
    permission_required = "references.add_bookseries"
    model = models.BookSeries
    form_class = forms.SeriesForm
    template_name = "references/edit_series.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["operation_name"] = "Create"
        return context


class UpdateSeries(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    login_url = "home_page:login"
    permission_required = "references.change_bookseries"
    model = models.BookSeries
    form_class = forms.SeriesForm
    template_name = "references/edit_series.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["operation_name"] = "Update"
        return context


class DeleteSeries(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    login_url = "home_page:login"
    permission_required = "references.delete_bookseries"
    model = models.BookSeries
    template_name = "references/delete_series.html"

    def get_success_url(self):
        return reverse_lazy("references:series_list")


class ShowGenres(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    login_url = "home_page:login"
    permission_required = "references.view_bookgenre"
    model = models.BookGenre
    template_name = "references/list_genre.html"


class ShowGenre(LoginRequiredMixin, PermissionRequiredMixin, generic.DetailView):
    login_url = "home_page:login"
    permission_required = "references.view_bookgenre"
    model = models.BookGenre
    template_name = "references/detail_genre.html"


class CreateGenre(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    login_url = "home_page:login"
    permission_required = "references.add_bookgenre"
    model = models.BookGenre
    form_class = forms.GenreForm
    template_name = "references/edit_genre.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["operation_name"] = "Create"
        return context


class UpdateGenre(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    login_url = "home_page:login"
    permission_required = "references.change_bookgenre"
    model = models.BookGenre
    form_class = forms.GenreForm
    template_name = "references/edit_genre.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["operation_name"] = "Update"
        return context


class DeleteGenre(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    login_url = "home_page:login"
    permission_required = "references.delete_bookgenre"
    model = models.BookGenre
    template_name = "references/delete_genre.html"

    def get_success_url(self):
        return reverse_lazy("references:genres_list")


class ShowHouses(generic.ListView):
    login_url = "home_page:login"
    model = models.BookPublishingHouse
    template_name = "references/list_house.html"


class ShowHouse(LoginRequiredMixin, PermissionRequiredMixin, generic.DetailView):
    login_url = "home_page:login"
    permission_required = "references.view_bookpublishinghouse"
    model = models.BookPublishingHouse
    template_name = "references/detail_house.html"


class CreateHouse(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    login_url = "home_page:login"
    permission_required = "references.add_bookpublishinghouse"
    model = models.BookPublishingHouse
    form_class = forms.PublishingHouseForm
    template_name = "references/edit_house.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["operation_name"] = "Create"
        return context


class UpdateHouse(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    login_url = "home_page:login"
    permission_required = "references.change_bookpublishinghouse"
    model = models.BookPublishingHouse
    form_class = forms.PublishingHouseForm
    template_name = "references/edit_house.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["operation_name"] = "Update"
        return context


class DeleteHouse(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    login_url = "home_page:login"
    permission_required = "references.delete_bookpublishinghouse"
    model = models.BookPublishingHouse
    template_name = "references/delete_house.html"

    def get_success_url(self):
        return reverse_lazy("references:houses_list")
