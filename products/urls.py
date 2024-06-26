from django.urls import path
from . import views

urlpatterns = [
    path("", views.view_products_list, name="products_list"),
    path("add_product/", views.view_add_product, name="add_product"),
    path('edit_product/<int:product_id>/', views.view_edit_product, name='edit_product'),
    path('delete_product/<int:product_id>/', views.view_delete_product, name='delete_product'),
    path("<slug:slug>/", views.view_product_details, name="product_details"),
    path("remove_rating/<slug:slug>/", views.view_remove_rating, name="remove_rating"),
    path("remove_rating/<slug:slug>/", views.view_remove_rating, name="remove_rating"),
    path("delete_product_review/<slug:slug>/<int:review_id>",
         views.view_delete_product_review, name="delete_product_review"),
    path("<slug:slug>/edit_product_review/<int:review_id>",
         views.view_edit_product_review, name="edit_product_review"),
]
