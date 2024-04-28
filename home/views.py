from django.shortcuts import render
from products.models import Product

def view_home_page(request):
    """
    View to render home page and 3 random products
    """
    random_products = Product.objects.order_by("?")[:3]

    context = {
        "random_products": random_products,
    }
    return render (request, "home/index.html", context)

def view_privacy(request):
    """
    View to render privacy page
    """
    return render (request, "home/privacy.html")


# Custom error views
def view_custom403(request, exception=None):
    """
    View to render error 403 page
    """
    return render(request, "403.html", status=403)


def view_custom404(request, exception=None):
    """
    View to render error 404 page
    """
    return render(request, "404.html", status=404)


def view_custom405(request, exception=None):
    """
    View to render error 405 page
    """
    return render(request, "405.html", status=405)


def view_custom500(request, exception=None):
    """
    View to render error 500 page
    """
    return render(request, "500.html", status=500)
