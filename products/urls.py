from django.urls import path
from . import views

urlpatterns = [
    path("", views.products_list, name="products"),
    path("<slug:slug>/", views.product_details, name="product_information"),

]