from django import forms
from .models import Products,Rproduct

class ProductFrom(forms.ModelForm):
    class Meta:
        model=Products
        fields=[
            'title','description','price','summary'
        ]

class RawFrom(forms.Form):
    title=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"your name "}))
    description=forms.CharField(widget=forms.Textarea(attrs={"rows":20,
                                                             "cols":100}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"abc@gmail.com "}))
    price=forms.DecimalField(initial=199.99)