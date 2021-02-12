"""Favorite models."""
from django.db import models
from apps.food.models import Product
from apps.users.models import MyUser


class FavoriteManager(models.Manager):
    """Product manager."""

    def add_or_remove_favorite(self, response):
        try:
            obj, created = Favorite.objects.get_or_create(
                email=MyUser.objects.filter(email=response["email"]).first(),
                base_product=Product.objects.filter(
                    id=response["searched_product_id"]
                ).first(),
                substitute=Product.objects.filter(id=response["substitute_id"]).first(),
            )
            if created:
                pass
            else:
                obj.delete()
        except Exception as error:
            print(error)


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
    objects = FavoriteManager()
