from .models import ProductReview, ProductRating
from django import forms

class RatingForm(forms.ModelForm):
    """
    Form for leaving product ratings
    """
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

class ReviewForm(forms.ModelForm):
    class Meta:
        """
        Form for writing product reviews
        """
        model = ProductReview
        fields = [
            "content",
        ]
        labels = {
            "content": "",
        }

        widgets = {
            """
            Widgets for the product review form input
            """
            "content": forms.TextInput(
                attrs={"class": "form-control form-field",
                       "placeholder": "Max 500 characters",}),
        }