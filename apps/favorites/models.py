"""Favorite models."""
from django.db import models
from apps.purbeurreweb.models import Product
from apps.users.models import MyUser


class Favorite(models.Model):
    """Favorite model."""

    email = models.ForeignKey(MyUser, on_delete=models.PROTECT)
    base_product = models.ForeignKey(
        Product, on_delete=models.PROTECT, related_name="base_favorites"
    )
    substitute = models.ForeignKey(
        Product, on_delete=models.PROTECT, related_name="favorites"
    )
