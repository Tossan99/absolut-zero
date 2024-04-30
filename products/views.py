from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required

from .models import Product, Category, Subcategory, ProductRating, ProductReview
from .forms import RatingForm, ReviewForm


def view_products_list(request):
    """ 
    Shows all products and handles sorting and search queries 
    """

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
    """ 
    Shows product details, rating, reviews
    """

    queryset = Product.objects.all()
    product = get_object_or_404(queryset, slug=slug)
    product_reviews = product.product_reviews.all().order_by("-created_on")

    user_rating = False
    if request.user.is_authenticated:
        user_rating = ProductRating.objects.filter(user=request.user, product=product).exists()

    if request.method == "POST":
        if "rating_form" in request.POST:
            rating_form = RatingForm(data=request.POST)
            if rating_form.is_valid() and request.user.is_authenticated:
                rating = rating_form.save(commit=False)
                rating.user = request.user
                rating.product = product
                rating.save()
                messages.add_message(request, messages.SUCCESS, "Product rating submitted")
                return HttpResponseRedirect(reverse("product_details", args=[slug]))
            else:
                messages.add_message(request, messages.ERROR, "Error rating product")

        if "review_form" in request.POST:
            review_form = ReviewForm(data=request.POST)
            if review_form.is_valid() and request.user.is_authenticated:
                review = review_form.save(commit=False)
                review.author = request.user
                review.product = product
                review.save()
                messages.add_message(request, messages.SUCCESS,
                                     "Review submitted and awaiting approval")
                return HttpResponseRedirect(reverse("product_details", args=[slug]))
            else:
                messages.add_message(request, messages.ERROR, "Error submitting review")

    rating_form = RatingForm()
    review_form = ReviewForm()

    context = {
        "product": product,
        "product_reviews": product_reviews,
        "review_form": review_form,
        "rating_form": rating_form,
        "user_rating": user_rating,
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


def view_delete_product_review(request, slug, review_id):
    """
    view to delete product review
    """
    review = get_object_or_404(ProductReview, pk=review_id)

    if review.author == request.user:
        review.delete()
        messages.add_message(request, messages.SUCCESS, "Product review deleted")
    else:
        messages.add_message(request, messages.ERROR, "Error deleting product review")

    return HttpResponseRedirect(reverse("product_details", args=[slug]))


def view_edit_product_review(request, slug, review_id):
    """
    View to edit product review
    """
    if request.method == "POST":
        queryset = Product.objects.all()
        product = get_object_or_404(queryset, slug=slug)
        review = get_object_or_404(ProductReview, pk=review_id)
        review_form = ReviewForm(data=request.POST, instance=review)

        if review_form.is_valid() and review.author == request.user:
            review = review_form.save(commit=False)
            review.product = product
            review.approved = False
            review.save()
            messages.add_message(request, messages.SUCCESS,
                                  "Product review edited and awaiting approval")
        else:
            messages.add_message(request, messages.ERROR, "Error editing product review")

    return HttpResponseRedirect(reverse("product_details", args=[slug]))
