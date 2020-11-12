from django.db import models
from apps.purbeurreweb.models import Product
from apps.users.models import Profile

class Favorite(models.Model):
    user = models.ManyToManyField(Profile)
    product = models.ManyToManyField(Product)
