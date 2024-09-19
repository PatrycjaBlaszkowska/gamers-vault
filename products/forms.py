from django import forms 
from .models import Product, Category, Subcategory, ProductReview
from .widgets import CustomClearableFileInput

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
    
    image = forms.ImageField(label='Image', required=True, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        category_choices = [(c.id, c.name) for c in categories]

        self.fields['category'].choices = category_choices


from django import forms
from .models import ProductReview

class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = ['title', 'rating', 'content']
        widgets = {
            'rating': forms.RadioSelect(choices=[(i, f"{i} Star") for i in range(1, 6)]),
        }

    def __init__(self, *args, **kwargs):
        """ Add placeholders, set labels, manage autofocus, and make fields required """
        super().__init__(*args, **kwargs)
        
        # Set custom placeholders
        placeholders = {
            'title': 'Title of your review',
            'content': 'Write your review here...',
        }
    
        # self.fields['title'].widget.attrs['autofocus'] = True

        for field in self.fields:
            self.fields[field].label = False  
            self.fields[field].required = True
