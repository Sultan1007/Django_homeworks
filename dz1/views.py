from django.shortcuts import render
from dz1.models import *


def get_all_product(request):
    products = Product.objects.all()

    data = {
        'products': products
    }

    return render(request, 'product.html', context=data)


def get_one_product(request, product):
    product = Product.objects.get(product=id)
    data = {
        'product': product
    }
    return render(request, 'product.html', context=data)
