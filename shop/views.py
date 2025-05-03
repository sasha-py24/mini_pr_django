from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Product, Categories
from .forms import ProductCreationForm, CategoriesCreationForm


from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView


from django.http import JsonResponse, HttpResponseRedirect
import datetime


class IndexView(TemplateView):
    template_name = 'index.html'
    model = Product
    context_object_name = 'products'  # == {'products': products}


class ProductCreationView(CreateView):
    template_name = 'product.html'
    model = Product
    form_class = ProductCreationForm
    success_url = '/'




class DeleteProductView(DeleteView):
    pass


