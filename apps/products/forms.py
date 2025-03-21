from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image']

    def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          for field_name, field in self.fields.items():
              field.widget.attrs['class'] = 'form-control'
              field.widget.attrs['placeholder'] = field.label