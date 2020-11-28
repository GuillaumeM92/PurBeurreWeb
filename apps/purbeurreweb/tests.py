"""Purbeurreweb tests."""
from django.test import TestCase
from .models import Product, Category


class ProductSubstituteTestCase(TestCase):
    """Test the product and substitutes."""

    def setUp(self):
        """Create and populate a testing database."""
        Category.objects.create(name="boisson")
        self.pepsi = Product.objects.create(id=1, name="pepsi", nutriscore="E")
        self.fanta = Product.objects.create(id=2, name="fanta", nutriscore="C")
        self.apple_juice = Product.objects.create(
            id=3, name="jus de pomme", nutriscore="B"
        )

        self.products = Product.objects.all()
        self.category = Category.objects.first()

        for product in self.products:
            product.categories.add(self.category)

    def test_substitute(self):
        """Check if a substitute is found and presented as expected."""
        product = self.pepsi
        expected_substitute = self.apple_juice

        found_substitute = Product.objects.get_substitutes(product).first()
        self.assertEqual(expected_substitute.id, found_substitute.id)
        print(f"Test 3 : Is {expected_substitute.id} equal to {found_substitute.id}?")

    def test_substitute_has_better_nutriscore(self):
        """Check if substitute has a better nutriscore."""
        product = self.pepsi
        substitute = Product.objects.get_substitutes(product).first()
        self.assertGreater(product.nutriscore, substitute.nutriscore)
        print(f"Test 3 : Is {product.nutriscore} greater than {substitute.nutriscore}?")

    def test_substitute_has_similar_category(self):
        """Check if substitute has a similar category."""
        product = self.pepsi
        substitute = Product.objects.get_substitutes(product).first()
        self.assertEqual(product.categories.first(), substitute.categories.first())
        print(
            f"Test 3 : Is {product.categories.first()}"
            " equal to {substitute.categories.first()}?"
        )
