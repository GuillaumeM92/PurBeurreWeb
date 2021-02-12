"""Food view."""
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product
from apps.favorites.models import Favorite


def home(request):
    """Return the home page."""
    return render(request, "food/home.html")

def index(request):
    MAIS POURQUOI EST-IL SI MECHANT ?
    # ...

def legal(request):
    """Return the home page."""
    return render(request, "food/legal.html")


class ProductListView(ListView):
    """Product list view."""

    model = Product
    template_name = "food/products.html"
    context_object_name = "searched_product"

    def get_queryset(self):
        """Return the user search query."""
        user_search = self.request.GET.get("user_query")
        self.searched_product = Product.objects.get_product_from_(user_search)
        return self.searched_product

    def get_context_data(self, **kwargs):
        """Return the context for the substitutes."""
        substitutes = Product.objects.get_substitutes(self.searched_product)
        favorites = Favorite.objects.all()

        context = super().get_context_data(**kwargs)
        context["products_list"] = substitutes
        context["favorites"] = favorites

        return context


class ProductDetailView(DetailView):
    """Product detail view."""

    model = Product
    template_name = "food/product_detail.html"
