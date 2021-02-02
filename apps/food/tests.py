"""Purbeurreweb tests."""
from django.test import TestCase
from .models import Product, Category
import time


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
        print(f"Test 1 : Is {expected_substitute.id} equal to {found_substitute.id} ?")

    def test_substitute_has_better_nutriscore(self):
        """Check if substitute has a better nutriscore."""
        product = self.pepsi
        substitute = Product.objects.get_substitutes(product).first()
        self.assertGreater(product.nutriscore, substitute.nutriscore)
        print(
            f"Test 2 : Is {product.nutriscore} greater than {substitute.nutriscore} ?"
        )

    def test_substitute_has_similar_category(self):
        """Check if substitute has a similar category."""
        product = self.pepsi
        substitute = Product.objects.get_substitutes(product).first()
        self.assertEqual(product.categories.first(), substitute.categories.first())
        print(
            f"Test 3 : Is {product.categories.first()} equal to {substitute.categories.first()} ?"
        )


############ SELENIUM TESTS #############
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common import exceptions

from apps.users.models import MyUser
from apps.favorites.models import Favorite

driver = WebDriver(
    executable_path="C:/Users/Guillaume/Desktop/Formation OPC/P8_merle_guillaume/apps/food/chromedriver_win32/chromedriver.exe"
)
driver.get("chrome://settings/clearBrowserData")


class UserStorySeleniumTest(StaticLiveServerTestCase):
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

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = driver
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def register(self):
        self.selenium.get("%s%s" % (self.live_server_url, "/register/"))
        username_input = self.selenium.find_element_by_name("email")
        username_input.send_keys("test@email.com")
        password_input = self.selenium.find_element_by_name("password1")
        password_input.send_keys("testing1234")
        password_input = self.selenium.find_element_by_name("password2")
        password_input.send_keys("testing1234")
        self.selenium.find_element_by_xpath('//button[@value="Register"]').click()
        self.assertEqual(
            "test@email.com", MyUser.objects.get(email="test@email.com").email
        )

    def login(self):
        self.selenium.get("%s%s" % (self.live_server_url, "/login/"))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys("test@email.com")
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys("testing1234")
        self.selenium.find_element_by_xpath('//button[@value="Log in"]').click()
        self.assertTrue(MyUser.objects.get(email="test@email.com").is_authenticated)

    def search_product(self):
        self.selenium.get("%s%s" % (self.live_server_url, "/"))
        search = self.selenium.find_element_by_id("search-middle")
        search.send_keys("pepsi")
        self.selenium.find_element_by_xpath('//input[@id="search-icon"]').click()
        # breakpoint()

    def add_favorite(self):
        self.selenium.get(
            "%s%s"
            % (
                self.live_server_url,
                "/products/?csrfmiddlewaretoken=rw0BQsfaLyiBL9OX1qeHYiSiaJwm74ISl02W9nNSLOXnd4b4StpRjI2hesjGy7vo&user_query=pepsi",
            )
        )
        self.selenium.find_element_by_name("add-favorite").click()
        time.sleep(1)
        self.assertEqual("pepsi", Favorite.objects.first().base_product.name)

    def remove_favorite(self):
        self.selenium.get("%s%s" % (self.live_server_url, "/favorites/"))
        self.selenium.find_element_by_name("remove-favorite").click()
        self.assertRaises(Favorite.DoesNotExist)

    def logout(self):
        self.selenium.get("%s%s" % (self.live_server_url, "/"))
        try:
            self.selenium.find_element_by_id("navbar-button").click()
            self.selenium.find_element_by_id("logout-icon").click()
        except exceptions.ElementNotInteractableException:
            self.selenium.find_element_by_id("logout-icon").click()
            self.assertFalse(
                MyUser.objects.get(email="test@email.com").is_authenticated
            )

    def test_all(self):
        self.register()
        self.login()
        self.search_product()
        breakpoint()
        self.add_favorite()
        self.remove_favorite()
        self.logout()


# python manage.py test apps.food.tests.MySeleniumTests.test_all
