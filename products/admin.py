from django.contrib import admin
from .models import Product, Category, Subcategory, ProductRating, ProductReview, DiscountProduct


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(ProductRating)
admin.site.register(ProductReview)
admin.site.register(DiscountProduct)
