from django.test import TestCase
from .models import Product

class ProductSubstituteTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name="pepsi", categories="boisson", nutriscore="E")
        Product.objects.create(name="fanta", categories="boisson", nutriscore="C")
        Product.objects.create(name="jus de pomme", categories="boisson", nutriscore="B")


    def test_get_queryset(self):
            # query = self.request.GET.get('query')
            query = 'pepsi'
            searched_product = Product.objects.filter(nom__icontains=query).first()
            return searched_product
            self.assertEqual(searched_product, 'pepsi')

    def test_get_context_data(self, **kwargs):              # check if subtistutes are found and presented as expected
        # query = self.request.GET.get('query')
        query = 'pepsi'
        searched_product = Product.objects.filter(name__icontains=query).first()

        if searched_product:
            searched_product_all_categories = searched_product.categories.all()
            query = Product.objects.filter(categories=searched_product_all_categories[0]).all()

            index = 0
            for category in searched_product_all_categories[1:]:
                if index < 2:
                    query = query.filter(categories=category).all()
                    index += 1

            sliced_query = query.order_by('nutriscore')[:24]

            context = super().get_context_data(**kwargs)
            context['products_list'] = sliced_query
            return context

        else:
            return None

        self.assertEqual(sliced_query, ({{name="jus de pomme", categories="boisson", nutriscore="B"}, {name="fanta", categories="boisson", nutriscore="C"}}))
