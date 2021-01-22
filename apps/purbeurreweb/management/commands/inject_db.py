from django.core.management.base import BaseCommand
from apps.purbeurreweb.models import Product, Category
from apps.favorites.models import Favorite
import requests
import django.db.utils


class Command(BaseCommand):
    help = "Populates the database with data from OpenFoodFacts.org"

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.products_counter = 0
        self.categories_counter = 0
        self.clean_counter = 0
        self.url = "https://fr.openfoodfacts.org/cgi/search.pl"
        self.params = {"action": "process", "page_size": 1000, "json": True, "page": 1}
        self.products = []
        self.categories = []
        self.categories_url = "https://fr.openfoodfacts.org/categories&json=True"

        for num in range(1, 8):
            self.params["page"] = num
            products = requests.get(self.url, self.params).json().get("products")

            if products:
                for product in products:
                    self.products.append(product)

        categories = requests.get(self.categories_url).json().get("tags")
        if categories:
            for category in categories:
                if category["products"] >= 1500:
                    self.categories.append(category)

    def inject_products(self):
        Favorite.objects.all().delete()
        Product.objects.all().delete()

        for product in self.products:
            try:
                obj, created = Product.objects.get_or_create(
                    name=product["product_name_fr"],
                    brand=product["brands"],
                    ingredients=product["ingredients_text_fr"],
                    allergens=product["allergens"],
                    nutriscore=product["nutrition_grades_tags"][0],
                    stores=product["stores"],
                    labels=product["labels"],
                    url=product["url"],
                    image=product["selected_images"]["front"]["display"]["fr"],
                )
                self.products_counter += 1

            except (KeyError, django.db.utils.IntegrityError) as e:
                print(e)
                pass

    def inject_categories(self):
        Category.objects.all().delete()

        for category in self.categories:
            try:
                obj, created = Category.objects.get_or_create(
                    name=category["name"],
                )
                self.categories_counter += 1

            except (KeyError, django.db.utils.IntegrityError) as e:
                print(e)
                pass

    def define_product_categories(self):
        for product in self.products:
            try:
                self.product_categories = (
                    product["categories"]
                    .replace("' ", "'")
                    .replace(", ", ",")
                    .split(",")
                )
                self.product_name = product["product_name_fr"]
            except KeyError as e:
                print(e)
                pass

            for category in self.categories:
                if category["name"] in self.product_categories:
                    try:
                        product = Product.objects.get(name=self.product_name)
                        cat = Category.objects.get(name=category["name"])
                        product.categories.add(cat)
                    except (AttributeError, Product.DoesNotExist) as e:
                        print(e)
                        print(self.product_name)
                        pass

    def clean_database(self):
        no_categories = Product.objects.filter(categories__isnull=True)
        for product in no_categories:
            product.delete()
            self.clean_counter += 1

    def handle(self, *args, **options):
        self.inject_products()
        self.inject_categories()
        self.define_product_categories()
        self.clean_database()

        print(f"{self.products_counter} products were added to the database.")
        print(f"{self.categories_counter} categories were added to the database.")
        print(f"{self.clean_counter} products were cleaned off the database.")

        no_categories = Product.objects.filter(categories__isnull=True).count()
        print(no_categories)


# from apps.purbeurreweb.models import Product
# a = Product.objects.filter(categories__isnull=True).count()
# b = Product.objects.filter(nutriscore__isnull=True).count()
# c = Product.objects.filter(name__isnull=True).count()
# d = Product.objects.all().count()
