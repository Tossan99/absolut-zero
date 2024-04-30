from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect

from checkout.models import Order
from .models import UserProfile
from .forms import UserProfileForm


def view_profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully")

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = "profiles/profile.html"
    context = {
        "form": form,
        "orders": orders,
        "on_profile_page": True
    }

    return render(request, template, context)


def view_order_history(request, order_number):
    """ Display the user's order history """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f"This is a past confirmation for order number {order_number}. "
        "A confirmation email was sent on the order date."
    ))

    context = {
        "order": order,
        "from_profile": True,
    }

    return render(request, "checkout/checkout_success.html", context)


def view_delete_profile(request):
    """
    Delete the user's profile.
    """
    if request.method == "POST":
        user = request.user
        user.delete()
        messages.success(request, "Profile successfully deleted")
    return HttpResponseRedirect(reverse("home"))
