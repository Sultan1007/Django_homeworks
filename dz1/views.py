from django.shortcuts import render, redirect

from dz1.forms import UserCreationForm, ProductForm, CategoryForm
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


def add_product(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        price = request.POST.get('price')
        category = request.POST.get('category')
        category = Category.objects.get(name=category)
        Product.objects.create(title=title, description=description, price=price, category=category)
        return redirect('/products/')
    return render(request, 'add.html', context={'form': ProductForm})


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(data=request.POST)
        if form.is_valid():
            name = request.POST.get('category_name')
            Category.objects.create(name=name)
            return redirect('/categories/')

    return render(request, 'add0.html')


def add(request):
    data = {
        'form': ProductForm()
    }
    return render(request, 'add1.html', context=data)


def main_page(request):
    return render(request, 'main.html')


def register(request):
    if request.method == "POST":
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            print('POST запрос без ошибок')
            return redirect('/admin/')
        else:
            print('POST запрос с ошибками')
            return render(request, 'register.html', context={'form': form})

    data = {
        'form': UserCreationForm()
    }
    print('GET запрос')
    return render(request, 'register.html', context=data)
