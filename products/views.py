from django.shortcuts import render
from products.models import Product, Category, Review
# Create your views here.
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
            'reviews': reviews
        }
        return render(request, 'products/details.html', context=data)