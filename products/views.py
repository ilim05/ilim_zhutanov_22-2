from django.shortcuts import render
from products.models import Product, Category, Review
# Create your views here.
def products_view(request):
    if request.method == "GET":
        products = [{
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'category': product.category
        } for product in Product.objects.all()]

        data = {
            'products': products
        }

        return render(request, 'products/products.html', context=data)


def categories_view(request):
    if request.method == "GET":
        category = Category.objects.all()
        data_1 = {
            'category': category
        }
        return render(request, 'categories/categories.html', context=data_1)


def detail_product_view(request, id):
    if request.method == "GET":
        products = Product.objects.get(id=id)
        reviews = Review.objects.filter(product_id=id)
        data = {
            'products': products,
            'category': products.category.name,
            'reviews': reviews
        }
        return render(request, 'products/details.html', context=data)