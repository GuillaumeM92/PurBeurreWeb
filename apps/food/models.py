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

        # Only keep products with equivalent or higher nutriscore
        searched_product_nutriscore = product.nutriscore
        self.products_with_higher_nutriscore = Product.objects.filter(
            nutriscore__lte=searched_product_nutriscore
        )
        # Select the categories of the searched product
        self.product_categories = product.categories.all()

        # Keep only substitutes that share some categories with the searched product
        for category in self.product_categories:
            self.similar_products = self.products_with_higher_nutriscore.filter(
                categories=category
            )
            print(len(self.similar_products))
            limit = 100
            if len(self.similar_products) < limit:
                break

        # Count number of shared categories between substitutes and searched product
        self.iterator = 1
        self.relevance_list = []
        self.names_list = []

        for product in self.similar_products:
            score = 0
            for category in self.product_categories:
                if category in product.categories.all():
                    score += 1
            self.relevance_list.append((product.name, score))

        # Store the results in an ordered list
        self.relevance_list.sort(reverse=1, key=lambda score: score[1])
        self.relevance_list = self.relevance_list[0:24]

        for product in self.relevance_list:
            self.names_list.append(product[0])

        # Exclude the substitutes that didn't make it to the list
        for product in self.similar_products:
            if product.name not in self.names_list:
                self.similar_products = self.similar_products.exclude(name=product.name)

        # Order the results by nutriscore
        substitutes = self.similar_products.order_by("nutriscore").order_by(
            "nutriscore"
        )

        # Send the results back to the view
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
    nutrition_facts = models.CharField(max_length=500)

    objects = ProductManager()

    def __str__(self):
        """Return the name."""
        return self.name

    def get_absolute_url(self):
        """Return the url and product PK."""
        return reverse("product-detail", kwargs={"pk": self.pk})
