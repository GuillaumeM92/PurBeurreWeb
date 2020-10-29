from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class Favorite(models.Model):
    product_name = models.CharField(max_length=500, unique=True, default='favorites')

# class ProductManager(models.Manager):
#     def get_queryset(self):
#         query = self.request.GET.get('query')
#         searched_product = Product.objects.filter(nom__icontains=query).first()
#         return searched_product

class Product(models.Model):
    name = models.CharField(max_length=500, unique=True)
    brand = models.CharField(max_length=500)
    ingredients = models.TextField()
    allergenes = models.CharField(max_length=500)
    nutriscore = models.CharField(max_length=50)
    shops = models.CharField(max_length=500)
    labels = models.TextField()
    categories = models.ManyToManyField(Category, related_name='products')
    favorites = models.ManyToManyField(Favorite, related_name='favorites', blank=True)
    off_link = models.CharField(max_length=500)
    image = models.CharField(max_length=500)
    # objects = ProductManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'pk': self.pk})
