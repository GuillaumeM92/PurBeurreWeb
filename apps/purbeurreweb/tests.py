from django.test import TestCase
from .models import Product

class ProductSubstituteTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name="pepsi", categories="boisson", nutriscore="E")
        Product.objects.create(name="fanta", categories="boisson", nutriscore="C")
        Product.objects.create(name="jus de pomme", categories="boisson", nutriscore="B")

    def test_get_context_data(self, **kwargs):              # check if subtistutes are found and presented as expected
        query = 'pepsi'

        Product.objects.get_context_data()

        self.assertEqual(sliced_query, ({{name="jus de pomme", categories="boisson", nutriscore="B"}, {name="fanta", categories="boisson", nutriscore="C"}}))
