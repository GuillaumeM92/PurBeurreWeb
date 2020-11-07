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

    def get_queryset(self):
        query = self.request.GET.get('query')
        searched_product = Product.objects.get_product(query)
        return searched_product

    def get_context_data(self, **kwargs):
        query = self.request.GET.get('query')
        substitutes = Product.objects.get_substitutes(query)

        context = super().get_context_data(**kwargs)
        context['products_list'] = substitutes
        return context

class ProductDetailView(DetailView):
    model = Product
    template_name = 'purbeurreweb/product_detail.html'
