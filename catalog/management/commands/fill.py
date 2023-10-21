from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        category_list = [
            {"pk": 1, 'name': 'Овощи', 'description': 'остатки'},
            {"pk": 2, 'name': 'Ягоды', 'description': 'остатки'},
            {"pk": 3, 'name': 'Фрукты', 'description': 'остатки'},
            {"pk": 4, 'name': 'Бакалея', 'description': 'остатки'},
            {"pk": 5, 'name': 'Гастрономия', 'description': 'новые поступления'},
        ]

        category_for_create = []
        for category_item in category_list:
            category_for_create.append(Category(**category_item))

        Category.objects.bulk_create(category_for_create)

        cat1 = Category.objects.get(pk=1)
        cat2 = Category.objects.get(pk=2)
        cat3 = Category.objects.get(pk=3)

        product_list = [
            {"pk": 1,
             "name": "Огурец",
             "description": "бакинский",
             "image": "",
             "category": cat1,
             "price": 200,
             "creation_data": "2023-10-21T11:51:45Z",
             "last_modified_date": "2023-10-21T11:51:50Z"},
            {"pk": 2,
             "name": "Помидор",
             "description": "краснодарский",
             "image": "",
             "category": cat1,
             "price": 300,
             "creation_data": "2023-10-21T11:53:56Z",
             "last_modified_date": "2023-10-21T11:53:58Z"},
            {"pk": 3,
             "name": "Яблоко",
             "description": "голд",
             "image": "",
             "category": cat3,
             "price": 250,
             "creation_data": "2023-10-21T12:08:17Z",
             "last_modified_date": "2023-10-21T12:08:19Z"},
            {"pk": 4,
             "name": "Брусника",
             "description": "лесная",
             "image": "",
             "category": cat2,
             "price": 600,
             "creation_data": "2023-10-21T13:14:11Z",
             "last_modified_date": "2023-10-21T13:14:13Z"},
            {"pk": 5,
             "name": "Земляника",
             "description": "полевая",
             "image": "",
             "category": cat2,
             "price": 750,
             "creation_data": "2023-10-21T13:16:54Z",
             "last_modified_date": "2023-10-21T13:16:56Z"},
        ]

        product_for_create = []

        for product_item in product_list:
            product_for_create.append(Product(**product_item))

        Product.objects.bulk_create(product_for_create)
