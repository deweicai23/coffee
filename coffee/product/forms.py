from django import forms
from product.models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(label='產品名稱', max_length=128)
    content = forms.CharField(label='產品介紹', widget=forms.Textarea)

    class Meta:
        model = Product
        fields = ['title', 'content']