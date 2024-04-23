from django.urls import path
from . import views

urlpatterns = [
    path("", views.view_products_list, name="products_list"),
    path("<slug:slug>/", views.view_product_details, name="product_details"),

]