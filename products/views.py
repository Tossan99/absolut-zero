from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category

def products_list(request):
    """ Shows all products and handles sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter anything")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

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