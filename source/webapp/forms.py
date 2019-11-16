from django import forms

from webapp.models import Product, Review


class ProductForm(forms.ModelForm):
    picture = forms.ImageField(label='Картинка', required=False)

    class Meta:
        model = Product
        exclude = []


class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = []

