from django.test import TestCase
from .models import Product, Category

class ProductSubstituteTestCase(TestCase):
    def setUp(self):
        Category.objects.create(name="boisson")
        self.pepsi = Product.objects.create(id = 1, name="pepsi", nutriscore="E")
        self.fanta = Product.objects.create(id = 2, name="fanta", nutriscore="C")
        self.apple_juice = Product.objects.create(id = 3, name="jus de pomme", nutriscore="B")

        self.products = Product.objects.all()
        self.category = Category.objects.first()

        for product in self.products:
            product.categories.add(self.category)


    def test_substitute(self):
        """ check if substitutes are found and presented as expected """
        product = self.pepsi
        expected_substitute = self.apple_juice

        found_substitute = Product.objects.get_substitutes(product).first()
        self.assertEqual(expected_substitute.id, found_substitute.id)

    def test_substitute_has_better_nutriscore(self):
        """ ... """
        product = product.objects.all().first()
        substitute = Product.objects.get_substitutes(product).first()
        self.assertGreater(product.nutriscore, product.nutriscore)
