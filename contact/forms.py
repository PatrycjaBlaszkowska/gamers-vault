from django import forms
from .models import ContactQuery
from checkout.models import Order, OrderLineItem


class ContactQueryForm(forms.ModelForm):
    class Meta:
        model = ContactQuery
        fields = ['name', 'email', 'query_type', 'order', 'message']

    def __init__(self, *args, **kwargs):
        user_orders = kwargs.pop('user_orders', None)
        super().__init__(*args, **kwargs)

        # Populate the 'order' field with product
        # names from related OrderLineItems
        if user_orders and user_orders.exists():
            order_choices = []
            for order in user_orders:
                line_items = order.lineitems.all()
                for item in line_items:
                    order_choices.append((order.id, f"{item.product.name}"))
            self.fields['order'].choices = order_choices
            # Set as required when orders are present
            self.fields['order'].required = True
        else:
            # If no orders, make the 'order' field
            # optional and hide it in the form
            self.fields['order'].choices = [('', 'No orders to choose from')]
            # Make it optional if no orders are available
            self.fields['order'].required = False

        # Set custom placeholders for other fields
        self.fields['message'].widget.attrs['placeholder'] = (
            'Write your message here...'
        )
        self.fields['name'].widget.attrs['autofocus'] = True

        # Set fields to not show labels
        for field in self.fields:
            self.fields[field].label = False

    def clean_order(self):
        """
        Allow the 'order' field to be empty if there are no choices.
        """
        order = self.cleaned_data.get('order')

        # If the order field is optional (no choices), return None
        if not self.fields['order'].required and order == '':
            return None

        return order
