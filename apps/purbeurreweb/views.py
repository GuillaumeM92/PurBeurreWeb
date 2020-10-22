from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from .models import Product

def home(request):
    return render(request, 'purbeurreweb/home.html')

class ProductListView(ListView):
    model = Product
    template_name = 'purbeurreweb/products.html'
    context_object_name = 'searched_product'

    def get_queryset(self):
        query = self.request.GET.get('query')
        searched_product = Product.objects.filter(nom__icontains=query).first()
        return searched_product

    def get_context_data(self, **kwargs):
        query = self.request.GET.get('query')
        searched_product = Product.objects.filter(nom__icontains=query).first()

        if searched_product:
            searched_product_all_categories = searched_product.categories.all()
            query = Product.objects.filter(categories=searched_product_all_categories[0]).all()

            index = 0
            for category in searched_product_all_categories[1:]:
                if index < 2:
                    query = query.filter(categories=category).all()
                    index += 1

            sliced_query = query.order_by('note_nutritionnelle')[:24]

            context = super().get_context_data(**kwargs)
            context['products_list'] = sliced_query
            return context

        else:
            return None

class ProductDetailView(DetailView):
    model = Product
    template_name = 'purbeurreweb/product_detail.html'
