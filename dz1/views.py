from django.shortcuts import render
from dz1.models import *


def get_all_products(request):
    products = Product.objects.all()
    print(products)
    data = {
        'products': products
    }

    return render(request, 'product.html', context=data)


def get_one_product(request, id):
    product = Product.objects.get(id=id)

    data = {
        'product': product,
        # 'reviews': reviews,
    }
    return render(request, 'detail.html', context=data)
