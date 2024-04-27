from .models import Product, ProductRating
from django import forms

class RatingForm(forms.ModelForm):
    class Meta:
        model = ProductRating
        fields = [
            "rating",
        ]

    def clean_rating(self):
        rating = self.cleaned_data["rating"]
        if rating < 1 or rating > 5:
            raise forms.ValidationError("Rating must be between 1 and 5.")
        return rating

   