from django.contrib import admin
from .models import Product, Category, Subcategory, ProductRating, ProductReview, DiscountProduct


admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(ProductRating)
admin.site.register(ProductReview)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "subcategory", "price",)
    fields = ("name", "category", "subcategory", "description",
              "volume", "price", "percentage", "sweetness",
              "bitterness", "body", "organic", "image")
    exclude = ("sku", "slug", "rating", "discount",
               "old_price")


@admin.register(DiscountProduct)
class DiscountProductAdmin(admin.ModelAdmin):
    fields = ("product", "discount_percentage")
    exclude = ("discount_price",)