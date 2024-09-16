from django import forms 
from .models import Product, Category, Subcategory

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        category_choices = [(c.id, c.name) for c in categories]

        self.fields['category'].choices = category_choices