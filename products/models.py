from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from django.utils.text import slugify
from django.utils.crypto import get_random_string


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name
    

class Subcategory(models.Model):

    class Meta:
        verbose_name_plural = 'Subbategories'
        
    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=100, null=True, blank=True)
    

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Product(models.Model):
    name = models.CharField(max_length=100, blank=False)
    subname = models.CharField(max_length=100, blank=True)
    category = models.ForeignKey(
        'Category', null=True, blank=False, on_delete=models.SET_NULL, related_name="product_category")
    subcategory = models.ForeignKey(
        'Subcategory', null=True, blank=False, on_delete=models.SET_NULL, related_name="product_subcategory")
    sku = models.CharField(max_length=10, blank=True, editable=False, unique=True)
    slug = models.SlugField(max_length=300, blank=True, editable=False, unique=True)
    description = models.TextField(max_length=2000, blank=True)
    volume = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10000)], blank=False) #Volume in ml
    price = models.DecimalField(max_digits=7, decimal_places=2, blank=False) #Price in sek
    percentage = models.DecimalField(max_digits=4, decimal_places=2, blank=False) #Alcohol percentage
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    sweetness = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    bitterness = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    body = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])



    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            """
            Generate a unique slug based on the name and timestamp and a unique sku
            """
            base_slug = slugify(self.name)
            timestamp = timezone.now().strftime('%Y%m%d%H%M%S')
            unique_slug = f"{base_slug}-{timestamp}"
            self.slug = unique_slug
        
        if not self.sku:
            self.sku = get_random_string(10).upper()

        super().save(*args, **kwargs)