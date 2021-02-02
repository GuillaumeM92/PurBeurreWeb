# from django.shortcuts import render
from django.views.generic import ListView
from .models import Favorite
from django.http import JsonResponse


class FavoritesListView(ListView):
    model = Favorite
    template_name = "favorites/favorite_products.html"
    context_object_name = "favorites"


def favorite(request):
    if request.method == "GET":
        response = request.GET
        Favorite.objects.add_or_remove_favorite(response)
        return JsonResponse("success", status=200, safe=False)
    else:
        return JsonResponse("error", status=400, safe=False)
