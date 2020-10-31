from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class Favorite(models.Model):
    product_name = models.CharField(max_length=500, unique=True, default='favorites')

class ProductManager(models.Manager):
    def get_queryset(self):
        query = self.request.GET.get('query')
        searched_product = Product.objects.filter(nom__icontains=query).first()
        return searched_product

    def get_context_data(self, **kwargs):
        query = self.request.GET.get('query')
        searched_product = Product.objects.filter(name__icontains=query).first()

        if searched_product:
            searched_product_all_categories = searched_product.categories.all()
            query = Product.objects.filter(categories=searched_product_all_categories[0]).all()

            index = 0
            for category in searched_product_all_categories[1:]:
                if index < 2:
                    query = query.filter(categories=category).all()
                    index += 1

            sliced_query = query.order_by('nutriscore')[:24]

            context = super().get_context_data(**kwargs)
            context['products_list'] = sliced_query
            return context

        else:
            return None

class Product(models.Model):
    name = models.CharField(max_length=500, unique=True)
    brand = models.CharField(max_length=500)
    ingredients = models.TextField()
    allergens = models.CharField(max_length=500)
    nutriscore = models.CharField(max_length=50)
    stores = models.CharField(max_length=500)
    labels = models.TextField()
    categories = models.ManyToManyField(Category, related_name='products')
    favorites = models.ManyToManyField(Favorite, related_name='favorites', blank=True)
    url = models.CharField(max_length=500)
    image = models.CharField(max_length=500)
    objects = ProductManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'pk': self.pk})
