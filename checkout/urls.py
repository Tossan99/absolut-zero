from django.urls import path
from . import views
from .webhooks import webhook


urlpatterns = [
    path("", views.view_checkout, name="checkout"),
    path("checkout_success/<order_number>", views.view_checkout_success, name="checkout_success"),
    path("cache_checkout_data/", views.view_cache_checkout_data, name="cache_checkout_data"),
    path("wh/", webhook, name="webhook"),
]