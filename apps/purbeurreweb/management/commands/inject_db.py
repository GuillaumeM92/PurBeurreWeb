from django.core.management.base import BaseCommand, CommandError
from apps.purbeurreweb.models import Product, Favorite, Category
import requests
import django.db.utils


class Command(BaseCommand):
    help = 'Populates the database with data from OpenFoodFacts.org'

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.counter = 0

        # self.json_db1 = requests.get(self.url, self.params)

        self.json_db1 = requests.get(
            'https://fr.openfoodfacts.org/cgi/search.pl?action=process&page_size=1000&json=True').json()
        self.json_db2 = requests.get(
            'https://fr.openfoodfacts.org/cgi/search.pl?action=process&page_size=1000&page=2&json=True').json()
        self.json_db3 = requests.get(
            'https://fr.openfoodfacts.org/cgi/search.pl?action=process&page_size=1000&page=3&json=True').json()
        self.json_db4 = requests.get(
            'https://fr.openfoodfacts.org/cgi/search.pl?action=process&page_size=1000&page=4&json=True').json()
        self.json_db5 = requests.get(
            'https://fr.openfoodfacts.org/cgi/search.pl?action=process&page_size=1000&page=5&json=True').json()
        # self.full_db = "self.json_db1['products'] + self.json_db2['products'] + self.json_db3['products'] + self.json_db4['products'] + self.json_db5['products']"
        self.full_db = {**self.json_db1, **self.json_db2, self.json_db3, self.json_db4, self.json_db5}

    def inject_products(self):

        Product.objects.all().delete()

        for product in eval(self.full_db):
            try:
                obj, created = Product.objects.get_or_create(name=product['product_name_fr'], brand=product['brands'], ingredients=product['ingredients_text_fr'], allergenes=product['allergens'],
                                                             nutriscore=product['nutrition_grades_tags'][0], shops=product['stores'], labels=product['labels'], off_link=product['url'], image=product['selected_images']['front']['display']['fr'])
                self.counter += 1

            except (KeyError, django.db.utils.IntegrityError) as e:
                print(e)
                pass

    def inject_categories(self):
        Category.objects.all().delete()

        for product in eval(self.full_db):
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

        for product in eval(self.full_db):
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
