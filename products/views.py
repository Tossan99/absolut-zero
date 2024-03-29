from django.shortcuts import render
from django.views import generic
from .models import Product, Category

def products_list(request):
    """ Shows all products with sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)