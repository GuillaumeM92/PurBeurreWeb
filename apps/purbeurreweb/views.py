from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product


def home(request):
    return render(request, "purbeurreweb/home.html")


class ProductListView(ListView):
    model = Product
    template_name = "purbeurreweb/products.html"
    context_object_name = "searched_product"

    def get_queryset(self):
        user_search = self.request.GET.get("query")
        self.searched_product = Product.objects.get_product_from_(user_search)
        return self.searched_product

    def get_context_data(self, **kwargs):
        substitutes = Product.objects.get_substitutes(self.searched_product)

        context = super().get_context_data(**kwargs)
        context["products_list"] = substitutes
        return context

    def get_product_id(self):
        favorite_product = self.request.GET.get("favorite")
        return favorite_product


class ProductDetailView(DetailView):
    model = Product
    template_name = "purbeurreweb/product_detail.html"
