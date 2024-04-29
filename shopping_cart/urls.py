from django.urls import path
from . import views

urlpatterns = [
    path("", views.view_shopping_cart, name="shopping_cart"),
    path("add/<item_id>/", views.view_add_to_shopping_cart, name="add_to_shopping_cart"),
    path("adjust/<item_id>/", views.view_adjust_shopping_cart, name="adjust_shopping_cart"),
    path("remove/<item_id>/", views.view_remove_from_shopping_cart,
         name="remove_from_shopping_cart"),
]
