"""Purbeurreweb models."""
from django.db import models
from django.urls import reverse


class Category(models.Model):
    """Category model."""

    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        """Return the name."""
        return self.name


class ProductManager(models.Manager):
    """Product manager."""

    def get_product_from_(self, search):
        """Return the first product matching the user search."""
        self.searched_product = Product.objects.filter(name__icontains=search).first()
        return self.searched_product

    def get_substitutes(self, product):
        """Return a list of substitutes corresponding to the searched product.

        Sort them by their nutriscore.
        """
        if not product:
            return None

        product_categories = product.categories.all()

        for category in product_categories:
            similar_products = Product.objects.all().filter(categories=category)
            minimum_required_length = 100
            if len(similar_products) < minimum_required_length:
                break

        max_displayed_subtitutes = 24
        substitutes = similar_products.order_by("nutriscore")[:max_displayed_subtitutes]

        return substitutes


class Product(models.Model):
    """Product model."""

    name = models.CharField(max_length=500, unique=True)
    brand = models.CharField(max_length=500)
    ingredients = models.TextField()
    allergens = models.CharField(max_length=500)
    nutriscore = models.CharField(max_length=50)
    stores = models.CharField(max_length=500)
    labels = models.TextField()
    categories = models.ManyToManyField(Category, related_name="products")
    url = models.CharField(max_length=500)
    image = models.CharField(max_length=500)
    objects = ProductManager()

    def __str__(self):
        """Return the name."""
        return self.name

    def get_absolute_url(self):
        """Return the url and product PK."""
        return reverse("product-detail", kwargs={"pk": self.pk})
