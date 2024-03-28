from django.shortcuts import render
from django.views import generic
from .models import Product, Category

class ProductList(generic.ListView):
    queryset = Product.objects.all()
    template_name = "products/products.html"