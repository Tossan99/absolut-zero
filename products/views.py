from django.shortcuts import render
from django.views import generic

class ProductList(generic.ListView):
    template_name = "products/products.html"