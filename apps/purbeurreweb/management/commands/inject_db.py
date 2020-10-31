from django.core.management.base import BaseCommand, CommandError
from apps.purbeurreweb.models import Product, Favorite, Category
import requests
import django.db.utils


class Command(BaseCommand):
    help = 'Populates the database with data from OpenFoodFacts.org'

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.counter = 0
        self.url = 'https://fr.openfoodfacts.org/cgi/search.pl'
        self.params = {'action': 'process', 'page_size': 10, 'json': True, 'page': 1}
        self.products = {}

        for num in range(1, 6):
            self.params["page_number"] = num
            products = requests.get(self.url, self.params).json().get("product")
            if products:
                self.products = {**self.products, **products[0]}

    def inject_products(self):

        Product.objects.all().delete()

        for product in self.products:
            try:
                obj, created = Product.objects.get_or_create(name=product['product_name_fr'], brand=product['brands'], ingredients=product['ingredients_text_fr'], allergens=product['allergens'],
                                                             nutriscore=product['nutrition_grades_tags'][0], stores=product['stores'], labels=product['labels'], url=product['url'], image=product['selected_images']['front']['display']['fr'])
                self.counter += 1

            except (KeyError, django.db.utils.IntegrityError) as e:
                print(e)
                pass

    def inject_categories(self):
        Category.objects.all().delete()

        for product in self.products:
            try:
                product_categories_list = product['categories'].replace(
                    "' ", "'").replace(", ", ",").split(',')
            except KeyError as e:
                print(e)
                pass

            for category in product_categories_list:
                try:
                    obj, created = Category.objects.get_or_create(
                        name=category)
                except KeyError as e:
                    print(e)
                    pass

    def define_product_categories(self):
        categories = Category.objects.values('name')

        categories_list = []
        iterator = 0

        for category in Category.objects.values('name'):
            cat = categories[iterator]['name']
            categories_list.append(cat)
            iterator += 1

        for product in self.products:
            try:
                product_categories_list = product['categories'].replace(
                    "' ", "'").replace(", ", ",").split(',')
                product_name = product['product_name_fr']
            except KeyError as e:
                print(e)
                pass

            for category in product_categories_list:
                if category in categories_list:
                    product = Product.objects.filter(name=product_name).first()
                    category = Category.objects.filter(name=category).first()
                    try:
                        product.categories.add(category)
                    except AttributeError as e:
                        print(e)
                        pass

    def handle(self, *args, **options):
        self.inject_products()
        self.inject_categories()
        self.define_product_categories()

        print(f'{self.counter} products were added to the database.')
