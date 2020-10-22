from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Categorie(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class Favorite(models.Model):
    product_name = models.CharField(max_length=500, unique=True, default='favoris')

class Product(models.Model):
    nom = models.CharField(max_length=500, unique=True)
    marque = models.CharField(max_length=500)
    ingrédients = models.TextField()
    allergènes = models.CharField(max_length=500)
    note_nutritionnelle = models.CharField(max_length=50)
    magasins = models.CharField(max_length=500)
    labels = models.TextField()
    categories = models.ManyToManyField(Categorie, related_name='products')
    favoris = models.ManyToManyField(Favorite, related_name='favorites', blank=True)
    lien_off = models.CharField(max_length=500)
    image = models.CharField(max_length=500)

    def __str__(self):
        return self.nom

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'pk': self.pk})
