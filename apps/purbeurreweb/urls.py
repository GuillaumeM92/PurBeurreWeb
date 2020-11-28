"""purbeurreweb urls."""
from django.urls import path
from .views import ProductListView, ProductDetailView
from . import views

urlpatterns = [
    path("", views.home, name="purbeurre-home"),
    path("products/", ProductListView.as_view(), name="purbeurre-products"),
    path("product/<int:pk>", ProductDetailView.as_view(), name="product-detail"),
]
