from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Product, Category

def products_list(request):
    """ Shows all products and handles sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_details(request, slug):
    """ Shows product details """
    
    queryset = Product.objects.all()
    product = get_object_or_404(queryset, slug=slug)
    related_products = Product.objects.all()

    context = {
        'product': product,
        'related_products': related_products,
    }

    return render(request, 'products/product_details.html', context)