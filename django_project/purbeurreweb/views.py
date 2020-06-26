from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'purbeurreweb/home.html')


def about(request):
    return render(request, 'purbeurreweb/about.html', {'title': 'About'})
