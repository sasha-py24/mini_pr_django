from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Product, Categories, Order
from .forms import ProductCreationForm, CategoriesCreationForm, OrderCreationForm


from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormMixin
from django.views.generic.detail import DetailView


from django.http import JsonResponse, HttpResponseRedirect
import datetime


class IndexView(ListView):
    template_name = 'index.html'
    model = Product
    context_object_name = 'products'  # == {'products': products}


class ProductCreationView(CreateView):
    template_name = 'product.html'
    model = Product
    form_class = ProductCreationForm
    success_url = '/'


class ProductCatalog(FormMixin, ListView):
    template_name = "catalog.html"
    model = Product
    context_object_name = 'products'
    form_class = OrderCreationForm



class OrderView(CreateView):
    form_class = OrderCreationForm

    def get_form_class(self):
        product = Product.objects.get(pk=self.kwargs['product_id'])
        kwargs = {
            'product': product
        }
        return kwargs



