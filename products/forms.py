from django import forms
from .models import ProductReview, ProductRating, Product, Category, Subcategory


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
                       "placeholder": "Max 500 characters", }),
        }


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        subcategories = Subcategory.objects.all()
        subcategories_friendly_names = [(c.id, c.get_friendly_name()) for c in subcategories]
        categories_friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields["category"].choices = categories_friendly_names
        self.fields["subcategory"].choices = subcategories_friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control form-field"
