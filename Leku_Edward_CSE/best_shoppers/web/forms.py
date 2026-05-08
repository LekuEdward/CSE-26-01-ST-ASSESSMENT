from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'price', 'quantity', 'color', 'image']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Product Name',
                'class': 'form-input',
                'required': True,
            }),
            'category': forms.TextInput(attrs={
                'placeholder': 'Category',
                'class': 'form-input',
                'required': True,
            }),
            'price': forms.NumberInput(attrs={
                'placeholder': 'Price',
                'class': 'form-input',
                'min': '1',
                'required': True,
            }),
            'quantity': forms.NumberInput(attrs={
                'placeholder': 'Quantity',
                'class': 'form-input',
                'min': '0',
                'required': True,
            }),
            'color': forms.TextInput(attrs={
                'placeholder': 'Color',
                'class': 'form-input',
                'required': True,
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-input file-input',
            }),
        }