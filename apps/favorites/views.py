# from django.shortcuts import render
from django.views.generic import ListView
from .models import Favorite
from django.http import JsonResponse
from apps.purbeurreweb.models import Product
from apps.users.models import MyUser


class FavoritesListView(ListView):
    model = Favorite
    template_name = "favorites/favorite_products.html"
    context_object_name = "favorites"


def favorite(request):
    if request.method == "GET" and request.is_ajax():
        response = request.GET
        add_favorite(response)
        return JsonResponse("success", status=200, safe=False)
    else:
        return JsonResponse("error", status=400, safe=False)


def rem_favorite(request):
    if request.method == "GET" and request.is_ajax():
        response = request.GET
        remove_favorite(response)
        return JsonResponse("success", status=200, safe=False)
    else:
        return JsonResponse("error", status=400, safe=False)


def add_favorite(response):
    try:
        obj, created = Favorite.objects.get_or_create(
            email=MyUser.objects.filter(email=response["email"]).first(),
            base_product=Product.objects.filter(
                id=response["searched_product_id"]
            ).first(),
            substitute=Product.objects.filter(id=response["substitute_id"]).first(),
        )
    except () as e:
        print(e)
        pass


def remove_favorite(response):
    try:
        fav = Favorite.objects.get(
            email=MyUser.objects.filter(email=response["email"]).first(),
            substitute=Product.objects.filter(id=response["substitute_id"]).first(),
        )
        fav.delete()
    except () as e:
        print(e)
        pass
