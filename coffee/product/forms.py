from django import forms
from product.models import Product,Order


class ProductForm(forms.ModelForm):
    title = forms.CharField(label='產品名稱', max_length=128)
    content = forms.CharField(label='產品介紹', widget=forms.Textarea)
    sale = forms.CharField(label='產品價格')

    class Meta:
        model = Product
        fields = ['title', 'content','sale']
        

class OrderForm(forms.ModelForm):
    fullName = forms.CharField(label='姓名',max_length=128)
    address = forms.CharField(label='住址', max_length=128)
    phone = forms.CharField(label='電話')
    number = forms.IntegerField(label='數量')
    
    
    class Meta:
        model = Order
        fields = ['fullName', 'address','phone','number']
        
        
        
                