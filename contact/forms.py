from django import forms
from .models import ContactQuery
from checkout.models import Order, OrderLineItem

from django import forms
from checkout.models import Order, OrderLineItem
from .models import ContactQuery  # Assuming ContactQuery is your model

class ContactQueryForm(forms.ModelForm):
    class Meta:
        model = ContactQuery
        fields = ['name', 'email', 'query_type', 'order', 'message']

    def __init__(self, *args, **kwargs):
        user_orders = kwargs.pop('user_orders', None)
        super().__init__(*args, **kwargs)

        # Populate the 'order' field with product names from related OrderLineItems
        if user_orders and user_orders.exists():
            # Create a list of tuples with the order's product name and order number
            order_choices = []
            for order in user_orders:
                # Get the related OrderLineItems
                line_items = order.lineitems.all()
                for item in line_items:
                    # Append product name with order number to the choices
                    order_choices.append((order.id, f"{item.product.name}"))

            self.fields['order'].choices = order_choices
        else:
            # If no orders, display a placeholder option
            self.fields['order'].choices = [('', 'No orders to choose from')]

        # Set custom placeholders for other fields
        self.fields['message'].widget.attrs['placeholder'] = 'Write your message here...'
        self.fields['name'].widget.attrs['autofocus'] = True

        # Set fields to not show labels and be required
        for field in self.fields:
            self.fields[field].label = False  
            self.fields[field].required = True
