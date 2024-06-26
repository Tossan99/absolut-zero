from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.text import slugify
from django.utils.crypto import get_random_string
from django.db.models import Avg, Count


class Category(models.Model):
    """
    Model to store categories
    """
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=100,
            help_text="Write the name in all lower case, no special characters and use - as blank spaces")
    friendly_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.friendly_name

    def get_friendly_name(self):
        return self.friendly_name


class Subcategory(models.Model):
    """
    Model to store subcategories
    """
    class Meta:
        verbose_name_plural = "Subbategories"

    name = models.CharField(max_length=100,
        help_text="Write the name in all lower case, no special characters and use - as blank spaces")
    friendly_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.friendly_name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """
    Model to store products
    """
    name = models.CharField(max_length=100, blank=False)
    category = models.ForeignKey(
        "Category", null=True, blank=False, on_delete=models.SET_NULL,
        related_name="product_category")
    subcategory = models.ForeignKey(
        "Subcategory", null=True, blank=False, on_delete=models.SET_NULL,
        related_name="product_subcategory")
    sku = models.CharField(max_length=10, blank=True, editable=False, unique=True,
        help_text="Leave this field empty, it will be set when creating the product")
    slug = models.SlugField(max_length=300, blank=True, editable=False, unique=True,
        help_text="Leave this field empty, it will be set when creating the product")
    description = models.TextField(max_length=2000, blank=False)
    volume = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10000)],
                                blank=False, help_text="Volume in ml")
    price = models.DecimalField(max_digits=7, decimal_places=2, blank=False,
                                help_text="Price in SEK")
    percentage = models.DecimalField(max_digits=4, decimal_places=2, blank=False,
                                    help_text="(e.g. 0,30 if 0.30%)")
    image = models.ImageField(null=True, blank=False)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    sweetness = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],
                                    help_text="On a scale from 1-10")
    bitterness = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],
                                    help_text="On a scale from 1-10")
    body = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],
                                help_text="On a scale from 1-10")
    organic = models.BooleanField(default=False)
    discount = models.BooleanField(default=False)
    old_price = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """
        Generate a unique sku and a slug based on the name and the sku
        """
        if not self.sku:
            self.sku = get_random_string(8).upper()

        if not self.slug:
            base_slug = slugify(self.name)
            sku = self.sku
            unique_slug = f"{base_slug}-{sku}"
            self.slug = unique_slug

        super().save(*args, **kwargs)

    def average_rating(self):
        """
        Calculates the avg rating for a product
        """
        reviews = ProductRating.objects.filter(product=self).aggregate(average=Avg("rating"))
        avg = 0
        if reviews["average"] is not None:
            avg = float(reviews["average"])
        return avg

    def count_rating(self):
        """
        Counts the amount of ratings for a product
        """
        reviews = ProductRating.objects.filter(product=self).aggregate(count=Count("id"))
        count = 0
        if reviews["count"] is not None:
            count = int(reviews["count"])
        return count


class ProductRating(models.Model):
    """
    Model for product ratings by users
    """
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f"{self.user} gave {self.product} a {self.rating} star rating"


class ProductReview(models.Model):
    """
    Model for product reviews by users
    """
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="product_reviewer")
    product = models.ForeignKey(
        "Product", on_delete=models.CASCADE, related_name="product_reviews")
    content = models.TextField(max_length=500, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)


class DiscountProduct(models.Model):
    """
    Model for discounts on products by site owner
    """
    product = models.ForeignKey(
        "Product", on_delete=models.CASCADE, related_name="discounts"
    )
    discount_price = models.DecimalField(
        max_digits=7, decimal_places=2, blank=True,
        help_text="Leave this field empty, it will be calculated based on the product price"
    )
    discount_percentage = models.DecimalField(
        max_digits=4, decimal_places=2, blank=False,
        help_text="The percentage discount applied to the product (e.g. 25 will give a 25% discount)"
    )

    def __str__(self):
        return f"{self.product.name} - {self.discount_percentage}% off"

    def save(self, *args, **kwargs):

        if self.discount_price is None:
            self.discount_price = self.product.price - (self.product.price *
                                                        (self.discount_percentage / 100))
        new_price = self.product.price - (self.product.price * (self.discount_percentage / 100))
        self.product.old_price = self.product.price
        self.product.price = new_price
        self.product.discount = True
        self.product.save()
        super().save(*args, **kwargs)
