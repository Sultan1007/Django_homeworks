from django.contrib import auth
from django.shortcuts import render, redirect

from dz1.forms import UserCreationForm, ProductForm, Product2Form, CategoryForm, LoginForm
from dz1.models import *

PAGE_SIZE = 3


def get_all_products(request):
    products = Product.objects.all()
    page = int(request.GET.get('page', 1))
    # reviews = Review.objects.get(product_id=id)
    print(products)
    # print(reviews)
    count = products.count()
    print(count // PAGE_SIZE)
    if count % PAGE_SIZE == 0:
        buttons = count // PAGE_SIZE
    else:
        buttons = count // PAGE_SIZE + 1
    print([i for i in range(1, buttons + 1)])
    start = (page - 1) * PAGE_SIZE
    end = page * PAGE_SIZE

    data = {
        'products': products[start:end],
        'username': auth.get_user(request).username,
        'buttons': [i for i in range(1, buttons + 1)],
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
    return render(request, 'add.html', context={'form': ProductForm, 'username': auth.get_user(request).username})


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(data=request.POST)
        if form.is_valid():
            name = request.POST.get('category_name')
            Category.objects.create(name=name)
            return redirect('/categories/')

    return render(request, 'add0.html', context={'username': auth.get_user(request).username})


def add(request):
    data = {
        'form': ProductForm()
    }
    return render(request, 'add1.html', context=data)


def main_page(request):
    data = {
        'username': auth.get_user(request).username
    }
    return render(request, 'main.html', context=data)


def register(request):
    if request.method == "POST":
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            print('POST запрос без ошибок')
            return redirect('/admin/')
        else:
            return render(request, 'register.html', context={'form': form})

    data = {
        'form': UserCreationForm(),
        'username': auth.get_user(request).username
    }
    print('GET запрос')
    return render(request, 'register.html', context=data)


def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = auth.authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                auth.login(request, user)
                return redirect('/')
        else:
            return render(request, 'login.html', context={'form': form})
    data = {
        'form': LoginForm(),
        'username': auth.get_user(request).username
    }
    return render(request, 'login.html', context=data)


def logout(request):
    auth.logout(request)
    return redirect('/')


def add_product2(request):
    if request.method == 'POST':
        form = Product2Form(data=request.POST)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('/products/')
        else:
            data = {
                'form': form,
                'username': auth.get_user(request).username
            }
            return render(request, 'add_product2.html', context=data)

    return render(request, 'add_product2.html',
                  context={'form': Product2Form})
    # data = {
    #     'form': Product2Form(),
    #     'username': auth.get_user(request).username
    # }
