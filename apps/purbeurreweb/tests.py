from django.test import TestCase
from .models import Product, Category

class ProductSubstituteTestCase(TestCase):
    def setUp(self):
        Category.objects.create(name="boisson")
        Product.objects.create(id = 1, name="pepsi", nutriscore="E")
        Product.objects.create(id = 2, name="fanta", nutriscore="C")
        Product.objects.create(id = 3, name="jus de pomme", nutriscore="B")

        self.products = Product.objects.all()
        self.category = Category.objects.first()

        for product in self.products:
            product.categories.add(self.category)


    def test_substitute(self):  # check if subtistutes are found and presented as expected
        query = "pepsi"
        searched_product = self.products.first()
        found_substitute = Product.objects.get_substitutes(query)
        self.assertEqual(searched_product.id, 1)
        self.assertEqual(found_substitute[0].id, 3)
