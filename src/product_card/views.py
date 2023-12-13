from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from . import models, forms
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class ShowProductCardList(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    login_url = "home_page:login"
    permission_required = "product_card.view_book"
    model = models.Book
    template_name = "product_card/list_pc.html"


class ShowProductCard(LoginRequiredMixin, PermissionRequiredMixin, generic.DetailView):
    login_url = "home_page:login"
    permission_required = "product_card.view_book"
    model = models.Book
    template_name = "product_card/detail_pc.html"


class CreateProductCard(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    login_url = "home_page:login"
    permission_required = "product_card.add_book"
    model = models.Book
    form_class = forms.ProductCardForm
    template_name = "product_card/edit_pc.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["operation_name"] = "Create"
        return context


class UpdateProductCard(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    login_url = "home_page:login"
    permission_required = "product_card.change_book"
    model = models.Book
    form_class = forms.ProductCardForm
    template_name = "product_card/edit_pc.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["operation_name"] = "Update"
        return context


class DeleteProductCard(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    login_url = "home_page:login"
    permission_required = "product_card.delete_book"
    model = models.Book
    template_name = "product_card/delete_pc.html"

    def get_success_url(self):
        return reverse_lazy("product_card:pc_list")
