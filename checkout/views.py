from django.shortcuts import render,redirect,reverse
from django.contrib import messages

from .forms import OrderForm

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in the bag at the moment!")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51PvkztJdgATrWI66IpAkKfDBE31XA5FlQ0zoMb6peQEe5oDDoIWwydWcDRFHbsbEzwKQI7hln4NEec0BUQ4lI7Jk00kg2GeFNY',
    }

    return render(request, template,context)