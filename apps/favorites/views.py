from django.shortcuts import render
from django.views.generic import ListView
from apps.purbeurreweb.models import Product
from .models import Favorite


class FavoritesListView(ListView):
    model = Product
    template_name = "favorites/favorite_products.html"
    context_object_name = "favorites"
    ordering = ["name"]

    # def get_favorite(self):
    #     user_favorite = self.request.GET.get('favorite')
    #     print('qsdsqdqsdqsdSQDQSDQSDSQDSQDqsdqsdqsdq')
    #     print(user_fav)
