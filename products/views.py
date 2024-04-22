from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, Subcategory
from django.db.models.functions import Lower

def products_list(request):
    """ Shows all products and handles sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    subcategories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split()
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
        
        if 'subcategory' in request.GET:
            subcategories = request.GET['subcategory'].split()
            products = products.filter(subcategory__name__in=subcategories)
            subcategories = Subcategory.objects.filter(name__in=subcategories)

        if "q" in request.GET:
            query = request.GET["q"]
            if not query:
                messages.error(request, "You didn't search for anything.")
                return redirect(reverse("products"))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        "products": products,
        "search_term": query,
        "current_categories": categories,
        "current_subcategories": subcategories,
        "current_sorting": current_sorting,
    }

    return render(request, "products/products.html", context)


def product_details(request, slug):
    """ Shows product details """
    
    queryset = Product.objects.all()
    product = get_object_or_404(queryset, slug=slug)
    related_products = Product.objects.all()

    context = {
        "product": product,
        "related_products": related_products,
    }

    return render(request, "products/product_details.html", context)