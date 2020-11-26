from django.db import models
from apps.purbeurreweb.models import Product
from apps.users.models import Profile

class ProductManager(models.Manager):

    # def get_product_from_(self, search):
    #     """ return the first product matching the user search """
    #     self.searched_product = Product.objects.filter(name__icontains=search).first()
    #     return self.searched_product
    pass

class Favorite(models.Model):
    user = models.ForeignKey(Profile)
    base_product = models.ForeignKey(Product)
    substitute = models.ForeignKey(Product)
    objects = ProductManager()


