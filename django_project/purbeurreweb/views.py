from django.shortcuts import render
from django.http import HttpResponse
from .models import FavoriteFood


def home(request):
    return render(request, 'purbeurreweb/home.html')


def produits(request):
    dummy_data = {
        'mock_food': FavoriteFood.objects.all()
    }
    return render(request, 'purbeurreweb/produits.html', dummy_data)
