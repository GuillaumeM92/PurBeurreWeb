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
        self.autocomplete_counter = 0
        self.url = "https://fr.openfoodfacts.org/cgi/search.pl"
        self.params = {"action": "process", "page_size": 1000, "json": True, "page": 1}
        self.categories = []
        self.categories_url = "https://fr.openfoodfacts.org/categories&json=True"
        self.all_product_names = []

        categories = requests.get(self.categories_url).json().get("tags")
        if categories:
            for category in categories:
                if category["products"] >= 1500:
                    self.categories.append(category)

    def inject_products(self):

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
                    nutrition_facts=product["selected_images"]["nutrition"]["display"][
                        "fr"
                    ],
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
        for product in Product.objects.all():
            if len(product.categories.all()) <= 1:
                product.delete()
                self.clean_counter += 1

    def create_product_list_for_autocompletetion_feature(self):
        doc = "apps/purbeurreweb/static/purbeurreweb/js/product_names_list.js"
        f = open(doc, "w")

        for product in Product.objects.all():
            try:
                self.all_product_names.append(
                    product.name.encode("cp1252").decode("cp1252")
                )
                self.autocomplete_counter += 1
            except ValueError as e:
                print(e)
                pass

        formatted = (
            str(self.all_product_names)
            .replace('"', "'")
            .replace("['", '["')
            .replace(", '", ', "')
            .replace("', ", '", ')
            .replace("']", '"]')
            .replace(', aux saveurs de  pommes", ', ", ")
        )
        f = open(doc, "w", encoding="utf-8")
        f.write("var products = ")
        f.write(formatted)

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Favorite.objects.all().delete()
        Product.objects.all().delete()

        self.inject_categories()

        for num in range(1, 50):
            self.products = []
            self.params["page"] = num
            try:
                products = requests.get(self.url, self.params).json().get("products")
            except ValueError as e:
                print(e)
                pass

            if products:
                for product in products:
                    self.products.append(product)

            self.inject_products()
            self.define_product_categories()

        self.clean_database()
        self.create_product_list_for_autocompletetion_feature()

        print(f"{self.products_counter} products were added to the database.")
        print(f"{self.categories_counter} categories were added to the database.")
        print(f"{self.clean_counter} products were cleaned off the database.")
        print(f"{self.autocomplete_counter} products added to the autocompletion list.")
