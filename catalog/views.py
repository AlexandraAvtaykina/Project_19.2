from django.shortcuts import render

from catalog.models import Category, Product


# Create your views here.

def index(request):
    product_list = Product.objects.all()
    context_prod = {
        'object_list_prod': product_list
    }
    return render(request, 'catalog/index.html', context_prod)


def contacts(request):
    return render(request, 'catalog/contacts.html')


def product(request):
    product_list = Product.objects.all()
    context_prod = {
        'object_list_prod': product_list
    }
    return render(request, 'catalog/product.html', context_prod)
