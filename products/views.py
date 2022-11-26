from django.shortcuts import render, redirect
from products.models import Product, Category, Review
from products.forms import ProductCreateForm, ReviewCreateForm

def products_view(request):
    if request.method == "GET":
        category_id = request.GET.get("category_id")
        if category_id:
            products = Product.objects.filter(categories__in=[category_id])
        else:
            products = Product.objects.all()
        products = [{
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'categories': product.categories.all()
        } for product in products]

        data = {
            'products': products
        }

        return render(request, 'products/products.html', context=data)


def categories_view(request, **kwargs):
    if request.method == "GET":
        categories = Category.objects.all()
        data = {
            'categories': categories
        }
        return render(request, 'categories/categories.html', context=data)


def detail_product_view(request, id):
    if request.method == "GET":
        products = Product.objects.get(id=id)
        reviews = Review.objects.filter(product_id=id)
        data = {
            'products': products,
            'categories': products.categories.name,
            'reviews': reviews,
            'form': ReviewCreateForm,
        }
        return render(request, 'products/details.html', context=data)
    if request.method == 'PRODUCT':
        form = ReviewCreateForm(data=request.PRODUCT)

        if form.is_valid():
            Review.objects.create(
                author_id=2,
                text=form.cleaned_data.get('text'),
                product_id=id,
            )
            return redirect('/products/{id}/')
        else:
            products = Product.objects.get(id=id)
            reviews = Review.objects.filter(product_id=id)
            data = {
                'products': products,
                'categories': products.categories.name,
                'reviews': reviews,
                'form': form,
            }
            return render(request, 'products/detail.html', context=data)

def product_create_form(request):
    if request.method == "GET":
        data = {
            'form': ProductCreateForm
        }
        return render(request, 'products/create.html', context=data)
    if request.method == 'PRODUCT':
        form = ProductCreateForm(data=request.PRODUCT)

        if form.is_valid():
            Product.objects.create(
                author_id=1,
                name=form.cleaned_data.get('name'),
                text=form.cleaned_data.get('text'),
                price=form.cleaned_data.get('price')
            )
            return redirect('/products')
        else:
            data = {
                'form': form
            }
            return render(request, 'products/create.html', context=data)