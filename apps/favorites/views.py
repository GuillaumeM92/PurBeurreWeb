# from django.shortcuts import render
from django.views.generic import ListView
from .models import Favorite
from django.http import JsonResponse


class FavoritesListView(ListView):
    model = Favorite
    template_name = "favorites/favorite_products.html"
    context_object_name = "favorites"
    ordering = ["name"]


def favorite(request):
    if request.method == "GET" and request.is_ajax():
        response = request.GET
        print(response)
        print(response["user"])
        return JsonResponse("good", status=200, safe=False)
    else:
        return JsonResponse("oops", status=400, safe=False)
