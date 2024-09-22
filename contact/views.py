from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactQueryForm
from checkout.models import Order
from profiles.models import UserProfile  

def contact(request):
    """ A view to return the contact page with a form """  
    user_orders = None
    if request.user.is_authenticated:
        try:
            user_profile = UserProfile.objects.get(user=request.user)
            user_orders = Order.objects.filter(user_profile=user_profile)
        except UserProfile.DoesNotExist:
            user_profile = None

    contact_form = ContactQueryForm(user_orders=user_orders)

    if request.method == 'POST':
        contact_form = ContactQueryForm(request.POST, user_orders=user_orders)
        if contact_form.is_valid():
            contact_form.save()
            return redirect('contact_success')
        else:
           messages.error(request, 'Failed to send contact query. Please ensure the form is valid.')

    context = {
        'contact_form': contact_form,
        'user_orders': user_orders,  
    }

    return render(request, 'contact/contact.html', context)


def contact_success(request):
    """ A view to render thank you page once user submit contact form """

    return render(request, 'contact/contact_success.html')