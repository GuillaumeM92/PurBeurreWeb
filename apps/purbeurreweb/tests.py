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


    def test_substitute(self):
        """ check if substitutes are found and presented as expected """
        user_search = "pepsi"
        searched_product = Product.objects.filter(name__icontains=user_search).first()

        expected_substitute = Product.objects.get(name="jus de pomme")

        found_substitute = Product.objects.get_substitutes(searched_product).first()
        self.assertEqual(expected_substitute.id, found_substitute.id)
