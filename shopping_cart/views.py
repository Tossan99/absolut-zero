from django.shortcuts import render, redirect, reverse, HttpResponse


def view_shopping_cart(request):
    return render (request, "shopping_cart/shopping_cart.html")

def view_add_to_shopping_cart(request, item_id):
    """Adds items to the shopping cart"""

    quantity = int(request.POST.get("quantity"))
    redirect_url = request.POST.get("redirect_url")
    shopping_cart = request.session.get("shopping_cart", {})

    if item_id in list(shopping_cart.keys()):
        shopping_cart[item_id] += quantity
    else:
        shopping_cart[item_id] = quantity

    request.session["shopping_cart"] = shopping_cart
    return redirect(redirect_url)

def view_adjust_shopping_cart(request, item_id):
    """Changes the quantity of products to the specified amount"""

    quantity = int(request.POST.get("quantity"))
    shopping_cart = request.session.get("shopping_cart", {})

    if quantity > 0:
        shopping_cart[item_id] = quantity
    else:
        shopping_cart.pop(item_id)

    request.session["shopping_cart"] = shopping_cart
    return redirect(reverse("shopping_cart"))

def view_remove_from_shopping_cart(request, item_id):
    """Removes items from shopping cart"""

    shopping_cart = request.session.get("shopping_cart", {})
    shopping_cart.pop(item_id)
    request.session["shopping_cart"] = shopping_cart 
    return redirect(reverse("shopping_cart"))
   