from django import forms
from .models import Product_sub_cat, Product_manager

class userForm(forms.ModelForm):
    class Meta:
        model=Product_sub_cat
        fields='__all__'
        
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product_sub_cat
        fields = ['productprice', 'productmodal', 'productimage', 'productram', 'product']
        widgets = {
            'productprice' : forms.TextInput(attrs={'class': 'form-control'}),
            'productmodal' : forms.TextInput(attrs={'class': 'form-control'}),
            'productimage' : forms.FileInput(attrs={'class': 'form-control'}),
            'productram' : forms.TextInput(attrs={'class': 'form-control'}),
            'product' : forms.Select(attrs={'class': 'form-control'}),
        }
      
        
class productmanager(forms.ModelForm):
    class Meta:
        model = Product_manager
        fields = ['fullname', 'mobile','email', 'password']
        widgets = {
            'fullname': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
    