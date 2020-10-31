from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from .models import Product


def home(request):
    return render(request, 'purbeurreweb/home.html')

class ProductListView(ListView):
    model = Product
    template_name = 'purbeurreweb/products.html'
    context_object_name = 'searched_product'

    Product.objects.get_queryset()
    Product.objects.get_context_data()

class ProductDetailView(DetailView):
    model = Product
    template_name = 'purbeurreweb/product_detail.html'
