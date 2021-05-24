from django.shortcuts import render
from dz1.models import *


def get_all_products(request):
    products = Product.objects.all()
    # reviews = Review.objects.get(product_id=id)
    print(products)
    # print(reviews)
    data = {
        'products': products,
        # 'reviews': reviews
    }

    return render(request, 'product.html', context=data)


def get_one_product(request, id):
    product = Product.objects.get(id=id)
    reviews = Review.objects.filter(product_id=id)

    data = {
        'product': product,
        'reviews': reviews,
    }
    return render(request, 'detail.html', context=data)
