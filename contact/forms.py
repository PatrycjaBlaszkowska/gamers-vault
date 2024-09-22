from django import forms
from .models import ContactQuery
from checkout.models import Order

class ContactQueryForm(forms.ModelForm):
    class Meta:
        model = ContactQuery
        fields = ['name', 'email', 'query_type', 'order', 'message']

    def __init__(self, *args, **kwargs):
        user_orders = kwargs.pop('user_orders', None)
        super().__init__(*args, **kwargs)

        # Add a placeholder option if there are no user orders
        if user_orders is not None and user_orders.exists():
            self.fields['order'].queryset = user_orders
        else:
            self.fields['order'].choices = [('', 'No orders to choose from')]  # Placeholder option

        # Set custom placeholders
        self.fields['message'].widget.attrs['placeholder'] = 'Write your message here...'
        self.fields['name'].widget.attrs['autofocus'] = True

        for field in self.fields:
            self.fields[field].label = False  
            self.fields[field].required = True

