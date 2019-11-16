from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import ProductForm, ProductReviewForm
from webapp.models import Product, Review


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


class ProductDelete(DeleteView):
    template_name = 'product/delete.html'
    model = Product
    context_object_name = 'product'

    def get_success_url(self):
        return reverse_lazy('webapp:index')


class ReviewCreate(CreateView):
    model = Review
    template_name = 'review/create.html'
    form_class = ProductReviewForm

    def get_product(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Product, pk=pk)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.product = self.get_product()
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        # return reverse_lazy('webapp:index')
        return reverse('webapp:product', kwargs={'pk': self.object.product.pk})


class ReviewEdit(UpdateView):
    model = Review
    template_name = 'review/update.html'
    form_class = ProductReviewForm
    context_object_name = 'review'

    def get_success_url(self):
        return reverse('webapp:product', kwargs={'pk': self.object.product.pk})


class ReviewDelete(DeleteView):
    model = Review

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('webapp:product', kwargs={'pk': self.object.product.pk})