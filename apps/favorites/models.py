"""Favorite models."""
from django.db import models
from apps.purbeurreweb.models import Product
from apps.users.models import Profile


class FavoriteManager(models.Manager):
    """Favorite manager."""

    # def get_product_from_(self, search):
    #     """ return the first product matching the user search """
    #     self.searched_product = Product.objects.filter(name__icontains=search).first()
    #     return self.searched_product
    pass


class Favorite(models.Model):
    """Favorite model."""

    user = models.ForeignKey(Profile, on_delete=models.PROTECT)
    base_product = models.ForeignKey(
        Product, on_delete=models.PROTECT, related_name="base_favorites"
    )
    substitute = models.ForeignKey(
        Product, on_delete=models.PROTECT, related_name="favorites"
    )
    objects = FavoriteManager()
