from django.urls import path
from . import views

urlpatterns = [
    path("", views.view_checkout, name="checkout"),
    path("checkout_success/<order_number>", views.view_checkout_success, name="checkout_success"),
]