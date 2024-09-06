from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from checkout.webhook_handler import StripeWH_Handler

import stripe

@require_POST
@csrf_exempt
def webhook(request):
    """ Listen for webhooks from Stripe """
    # Setup
    wh_secret = settings.STRIPE_WEBHOOK_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # Get the webhook data and verify the signature
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, wh_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)
    except Exception as e:
        # General exception
        return HttpResponse(content=str(e), status=400)

    # Set up a webhook handler 
    handler = StripeWH_Handler(request)

    # Map webhook events to relevant handler functions
    event_map = {
        'payment_intent.succeeded': handler.handle_payment_intent_succeeded,
        'payment_intent.payment_failed': handler.handle_payment_intent_payment_failed,
    }

    # Get the webhook type from Stripe
    event_type = event['type']

    # If there's a handler for it, get it from the event map
    # Use the generic one by default
    event_handler = event_map.get(event_type, handler.handle_event)

    # Call the event handler with the event 
    response = event_handler(event)
    return response


class StripeWH_Handler:
    """ Handle Stripe webhooks """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """ Handle a generic/unknown/unexpected webhook event """
        return HttpResponse(
            content=f'Unhandled webhook received {event["type"]}',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """ Handle the payment_intent.succeeded webhook from Stripe """
        intent = event.data.object
        print(intent)
        return HttpResponse(
            content=f'Webhook received {event["type"]}',
            status=200
        )

    def handle_payment_intent_payment_failed(self, event):
        """ Handle the payment_intent.payment_failed webhook from Stripe """
        return HttpResponse(
            content=f'Webhook received {event["type"]}',
            status=200
        )
