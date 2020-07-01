"""purbeurreweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from .views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView
from . import views

urlpatterns = [
    path('', views.home, name="purbeurre-home"),
    path('products/', ProductListView.as_view(), name="purbeurre-products"),
    path('product/<int:pk>', ProductDetailView.as_view(), name="product-detail"),
    path('product/new/', ProductCreateView.as_view(), name="product-create"),
    path('product/<int:pk>/update',
         ProductUpdateView.as_view(), name="product-update"),
    path('product/<int:pk>/delete',
         ProductDeleteView.as_view(), name="product-delete"),
]
