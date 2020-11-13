from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class ProductManager(models.Manager):

    def get_product_from_(self, search):
        """ return the first product matching the user search """
        self.searched_product = Product.objects.filter(name__icontains=search).first()
        return self.searched_product

    def get_substitutes(self, product):
        """ returns a list of substitutes corresponding to the searched product, and sorts them by their nutriscore. """

        if not product:
            return None

        """ get all products which have the same category as the searched product's first category """
        product_categories = product.categories.all()
        most_relevant_category = product_categories.first()
        similar_products = Product.objects.filter(categories=most_relevant_category).all()

        for category in product_categories:
            print(len(product_categories))
            print(len(similar_products))

            minimum_required_length = 100
            if len(similar_products) > minimum_required_length:
                """ filter products based off the number of matching categories """
                similar_products = similar_products.filter(categories=category).all()

        max_displayed_subtitutes = 24
        substitutes = similar_products.order_by('nutriscore')[:max_displayed_subtitutes]

        return substitutes

class Product(models.Model):
    name = models.CharField(max_length=500, unique=True)
    brand = models.CharField(max_length=500)
    ingredients = models.TextField()
    allergens = models.CharField(max_length=500)
    nutriscore = models.CharField(max_length=50)
    stores = models.CharField(max_length=500)
    labels = models.TextField()
    categories = models.ManyToManyField(Category, related_name='products')
    url = models.CharField(max_length=500)
    image = models.CharField(max_length=500)
    objects = ProductManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'pk': self.pk})
