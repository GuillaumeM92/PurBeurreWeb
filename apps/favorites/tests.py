from django.test import TestCase, Client
from django.test.client import RequestFactory
from apps.food.models import Product, Category
from .models import Favorite
from apps.users.models import MyUser
from .views import favorite
from django.http import QueryDict


class AddRemoveFavoriteTestCase(TestCase):
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

        self.new_user = MyUser.objects.create_user("test@email.com", "testing1234")

        self.fake_ajax_response = RequestFactory().get(
            "/favorite/",
            {
                "searched_product_id": ["1"],
                "substitute_id": ["2"],
                "is_authenticated": ["True"],
                "email": ["test@email.com"],
                "status": ["add-favorite"],
            },
        )

    def test_add_favorite(self):

        """Check if adding a favorite works."""
        favorite(self.fake_ajax_response)
        self.assertEqual(
            self.pepsi.name, Favorite.objects.get(id="1").base_product.name
        )

    def test_remove_favorite(self):
        """Check if removing a favorite works."""
        favorite(self.fake_ajax_response)
        self.assertRaises(Favorite.DoesNotExist)
