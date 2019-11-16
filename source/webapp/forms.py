from django import forms

from webapp.models import Product


class ProductForm(forms.ModelForm):
    picture = forms.ImageField(label='Картинка', required=False)

    class Meta:
        model = Product
        exclude = []
