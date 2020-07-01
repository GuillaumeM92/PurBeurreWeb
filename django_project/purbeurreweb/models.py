from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Product(models.Model):
    nom = models.CharField(max_length=100)
    marque = models.CharField(max_length=100)
    ingrédients = models.TextField()
    allergènes = models.CharField(max_length=100)
    note_nutritionnelle = models.CharField(max_length=50)
    magasins = models.CharField(max_length=150)
    labels = models.TextField()
    lien_off = models.CharField(max_length=150)
    image = models.CharField(max_length=150)

    def __str__(self):
        return self.nom

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'pk': self.pk})


"""class Food(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('food-detail', kwargs={'pk': self.pk})"""
