from django.core.management.base import BaseCommand
from apps.purbeurreweb.models import Product


class Command(BaseCommand):
    help = "Populates the database with data from OpenFoodFacts.org"

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.all_product_names = []
        self.counter = 0

    def create_product_list_for_autocompletetion_feature(self):
        f = open("apps/purbeurreweb/static/purbeurreweb/js/product_names_list.js", "w")
        for product in Product.objects.all():
            self.all_product_names.append(
                product.name.encode("cp1252", "ignore")
                .decode("cp1252", "ignore")
                .encode("utf8", "ignore")
                .decode("utf8", "ignore")
            )
            self.counter += 1
        f.write("var products = ")
        f.write(str(self.all_product_names))
        print()

    def decode(self):
        f = open("apps/purbeurreweb/static/purbeurreweb/js/product_names_list.js", "r")
        print(f.read())

    def handle(self, *args, **options):
        self.create_product_list_for_autocompletetion_feature()
        self.decode()

        print(f"{self.counter} added to the autocompletion list.")
