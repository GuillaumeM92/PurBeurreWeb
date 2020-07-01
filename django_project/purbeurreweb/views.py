from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product


def home(request):
    return render(request, 'purbeurreweb/home.html')


class ProductListView(ListView):
    model = Product
    template_name = 'purbeurreweb/products.html'
    ordering = ['-nom']
    context_object_name = 'products'

    def get_queryset(self):
        query = self.request.GET.get('q')
        products_list = Product.objects.filter(nom__icontains=query)
        return products_list


class ProductDetailView(DetailView):
    model = Product
    template_name = 'purbeurreweb/product_detail.html'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['nom', 'marque']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    fields = ['nom', 'marque']
    template_name = 'purbeurreweb/product_update.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProductDeleteView(DeleteView):
    model = Product
    success_url = '/'
