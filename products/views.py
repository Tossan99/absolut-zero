from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, Subcategory, ProductRating
from django.db.models.functions import Lower
from .forms import RatingForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

def view_products_list(request):
    """ Shows all products and handles sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    subcategories = None
    sort = None
    direction = None

    if request.GET:
        if "sort" in request.GET:
            sortkey = request.GET["sort"]
            sort = sortkey
            if sortkey == "name":
                sortkey = "lower_name"
                products = products.annotate(lower_name=Lower("name"))
            if sortkey == "category":
                sortkey = "category__name"
            if "direction" in request.GET:
                direction = request.GET["direction"]
                if direction == "desc":
                    sortkey = f"-{sortkey}"
            products = products.order_by(sortkey)

        if "category" in request.GET:
            categories = request.GET["category"].split()
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
        
        if "subcategory" in request.GET:
            subcategories = request.GET["subcategory"].split()
            products = products.filter(subcategory__name__in=subcategories)
            subcategories = Subcategory.objects.filter(name__in=subcategories)

        if "q" in request.GET:
            query = request.GET["q"]
            if not query:
                messages.error(request, "You didn't search for anything.")
                return redirect(reverse("products_list"))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f"{sort}_{direction}"

    context = {
        "products": products,
        "search_term": query,
        "current_categories": categories,
        "current_subcategories": subcategories,
        "current_sorting": current_sorting,
        "direction": direction,
        "sort": sort,
    }

    return render(request, "products/products.html", context)


def view_product_details(request, slug):
    """ Shows product details """
    
    queryset = Product.objects.all()
    product = get_object_or_404(queryset, slug=slug)
    related_products = Product.objects.all()

    if request.user.is_authenticated:
        user_rating = ProductRating.objects.filter(user=request.user, product=product).exists()
    else:
        user_rating = False

    if request.method == "POST":
        rating_form = RatingForm(data=request.POST)
        if rating_form.is_valid() and request.user.is_authenticated:
            rating = rating_form.save(commit=False)
            rating.user = request.user
            rating.product = product
            rating.save()
            messages.add_message(request, messages.SUCCESS, 'Product rating submitted')
            return HttpResponseRedirect(reverse("product_details", args=[slug]))
        else:
            messages.add_message(request, messages.ERROR, 'Error rating product')
    
    rating_form = RatingForm()

    context = {
        "product": product,
        "rating_form": rating_form,
        "user_rating": user_rating,
        "related_products": related_products,
    }

    return render(request, "products/product_details.html", context)


@login_required
def view_remove_rating(request, slug):
    if request.method == "POST":
        product = get_object_or_404(Product, slug=slug)
        user = request.user
        rating = get_object_or_404(ProductRating, product=product, user=user)
        rating.delete()
        messages.success(request, "Your rating has been removed.")

    return HttpResponseRedirect(reverse("product_details", args=[slug]))
