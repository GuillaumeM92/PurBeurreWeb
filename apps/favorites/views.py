from django.shortcuts import render
from django.views.generic import ListView
from apps.purbeurreweb.models import Product

class FavoritesListView(ListView):
    model = Product
    template_name = 'favorites/favorite_products.html'
    context_object_name = 'favorites'
    # ordering = ['name']
