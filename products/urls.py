from django.urls import path
from products.views import products_view, categories_view, detail_product_view
from products.views import product_create_form


urlpatterns = [
    path('products/', products_view),
    path('category/', categories_view),
    path('products/<int:id>/', detail_product_view),
    path('products/create/', product_create_form),
]

