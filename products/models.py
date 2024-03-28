from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    name = models.CharField(max_length=100, blank=False)
    category = models.ForeignKey(
        'Category', null=True, blank=False, on_delete=models.CASCADE, related_name="product_category")
    description = models.TextField(max_length=1000, blank=True)
    volume = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10000)], blank=False) #Volume in ml
    price = models.DecimalField(max_digits=7, decimal_places=2, blank=False) #Price in sek

    def __str__(self):
        return self.name