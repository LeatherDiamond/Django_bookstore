from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from . import models, forms

# Create your views here.

class ShowProductCardList(generic.ListView):
    model = models.Book
    template_name = 'product_card/list_pc.html'


class ShowProductCard(generic.DetailView):
    model = models.Book
    template_name = 'product_card/detail_pc.html'


class CreateProductCard(generic.CreateView):
    model = models.Book
    form_class = forms.ProductCardForm
    template_name = 'product_card/edit_pc.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Create'
        return context


class UpdateProductCard(generic.UpdateView):
    model = models.Book
    form_class = forms.ProductCardForm
    template_name = 'product_card/edit_pc.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Update'
        return context


class DeleteProductCard(generic.DeleteView):
    model = models.Book
    template_name = 'product_card/delete_pc.html'

    def get_success_url(self):
        return reverse_lazy('product_card:pc_list')