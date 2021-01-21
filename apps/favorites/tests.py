from django.test import TestCase
from apps.purbeurreweb.models import Product, Category
from .models import Favorite
from apps.users.models import MyUser
from .views import add_or_remove_favorite
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

        self.fake_ajax_response = {
            "searched_product_id": ["176"],
            "substitute_id": ["4689"],
            "is_authenticated": ["True"],
            "email": ["gemacx@gmail.com"],
            "status": ["add-favorite"],
        }
        # self.fake_query_dict = QueryDict("", mutable=True)
        # self.fake_query_dict.update(self.fake_ajax_response)
        self.fake_ajax_response = QueryDict(
            "searched_product_id=1&substitute_id=2&is_authenticated=True&email=test@email.com&status=add-favorite"
        )

    def test_add_favorite(self):
        """Check if adding a favorite works."""
        add_or_remove_favorite(self.fake_ajax_response)
        self.assertEqual("pepsi", Favorite.objects.get(id="1").base_product.name)

    def test_remove_favorite(self):
        """Check if removing a favorite works."""
        add_or_remove_favorite(self.fake_ajax_response)
        add_or_remove_favorite(self.fake_ajax_response)
        self.assertRaises(Favorite.DoesNotExist)


# python manage.py test apps.favorites.tests
# all_favs = Favorite.objects.all()
# all_favs
# first_fav = all_favs.first()
# first_fav
