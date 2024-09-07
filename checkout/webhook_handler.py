from django.http import HttpResponse
from .models import Order, OrderLineItem
from products.models import Product

import json
import time

class StripeWH_Handler:
    """ Handle Stripe webhooks """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """ Handle a generic/unknown/unexpected webhook event """
        return HttpResponse(
            content=f'Unhandled webhook recived {event["type"]}',
            status=200
        )


def handle_payment_intent_succeeded(self, event):
    """ Handle the payment_intent.succeeded webhook from Stripe """
    intent = event.data.object
    pid = intent.id
    bag = intent.metadata.bag
    save_info = intent.metadata.save_info

    # Get the Charge object
    stripe_charge = stripe.Charge.retrieve(intent.latest_charge)

    billing_details = stripe_charge.billing_details
    shipping_details = intent.shipping
    grand_total = round(stripe_charge.amount / 100, 2)

    # Clean data in shipping details
    for field, value in shipping_details.address.items():
        if value == '':
            shipping_details.address[field] = None

    # Check if order exists
    order_exists = False
    attempt = 1
    while attempt <= 5:
        try:
            order = Order.objects.get(
                full_name__iexact=shipping_details.name,
                email__iexact=billing_details.email,
                phone_number__iexact=shipping_details.phone,
                country__iexact=shipping_details.address.country,
                postcode__iexact=shipping_details.address.postal_code,
                town_or_city__iexact=shipping_details.address.city,
                street_address1__iexact=shipping_details.address.line1,
                street_address2__iexact=shipping_details.address.line2,
                county__iexact=shipping_details.address.state,
                grand_total=grand_total,
                original_bag=bag,
                stripe_pid=pid,
            )
            order_exists = True
            break
        except Order.DoesNotExist:
        # Order does not exist, create it
            attempt +=1
            time.sleep(1)
        if order_exists:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database.',
                status=200
            )
        else :
            order = None
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    town_or_city=shipping_details.address.city,
                    street_address1=shipping_details.address.line1,
                    street_address2=shipping_details.address.line2,
                    county=shipping_details.address.state,
                    grand_total=grand_total,
                    original_bag=bag,
                    stripe_pid=pid,
                )

                # Create order line items
                for item_id, quantity in json.loads(bag).items():
                    product = Product.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=quantity,
                    )
                    order_line_item.save()

            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {str(e)}',
                    status=500
                )

    return HttpResponse(
        content=f'Webhook received: {event["type"]} | Order processed successfully.',
        status=200
    )

    def handle_payment_intent_payment_failed(self, event):
        """ Handle the payment_intent_payment_failed webhook from Stripe """
        return HttpResponse(
            content=f'Webhook recived {event["type"]}',
            status=200
        )