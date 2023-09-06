from django import forms
from .models import ShoppingCart

class CartUploadForm(forms.ModelForm): 
    
    class Meta:
        model = ShoppingCart
        fields = "__all__"
