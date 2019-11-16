from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from webapp.forms import ProductForm
from webapp.models import Product


class IndexView(ListView):
    context_object_name = 'products'
    template_name = 'product/index.html'
    model = Product


class ProductView(DetailView):
    pk_url_kwarg = 'pk'
    model = Product
    template_name = 'product/product.html'
    context_object_name = 'product'


class ProductCreate(CreateView):
    model = Product
    template_name = 'product/product_create.html'
    form_class = ProductForm

    def get_success_url(self):
        return reverse('webapp:product', kwargs={'pk': self.object.pk})


class ProductUpdate(UpdateView):
    form_class = ProductForm
    template_name = 'product/update.html'
    model = Product
    context_object_name = 'product'

    def get_success_url(self):
        return reverse('webapp:product', kwargs={'pk': self.object.pk})
