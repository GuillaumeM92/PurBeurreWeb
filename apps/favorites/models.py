"""Favorite models."""
from django.db import models
from apps.purbeurreweb.models import Product
from apps.users.models import Profile


class Favorite(models.Model):
    """Favorite model."""

    user = models.ForeignKey(Profile, on_delete=models.PROTECT)
    base_product = models.ForeignKey(
        Product, on_delete=models.PROTECT, related_name="base_favorites"
    )
    substitute = models.ForeignKey(
        Product, on_delete=models.PROTECT, related_name="favorites"
    )

    def __str__(self):
        return self.name
