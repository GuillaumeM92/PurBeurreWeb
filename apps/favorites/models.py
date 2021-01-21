"""Favorite models."""
from django.db import models
from apps.purbeurreweb.models import Product
from apps.users.models import MyUser


class FavoriteManager(models.Manager):
    """Favorite manager."""

    pass


class Favorite(models.Model):
    """Favorite model."""

    email = models.ForeignKey(
        MyUser, on_delete=models.PROTECT, related_name="favorite_email"
    )
    base_product = models.ForeignKey(
        Product, on_delete=models.PROTECT, related_name="favorite_base_product"
    )
    substitute = models.ForeignKey(
        Product, on_delete=models.PROTECT, related_name="favorite_substitute"
    )
