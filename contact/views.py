from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactQueryForm
from checkout.models import Order
from profiles.models import UserProfile  

def contact(request):
    """ 
    A view to handle the contact page with a form.
    Authenticated users can see their previous orders. 
    Handles both GET and POST requests.
    """
    
    # Check if user is authenticated and get their previous orders
    user_orders = None
    if request.user.is_authenticated:
        try:
            user_profile = UserProfile.objects.get(user=request.user)
            user_orders = Order.objects.filter(user_profile=user_profile)
            # Pre-fill the form with user data
            contact_form = ContactQueryForm(initial={
                'name': request.user.get_full_name(),
                'email': request.user.email
            }, user_orders=user_orders)
        except UserProfile.DoesNotExist:
            contact_form = ContactQueryForm(user_orders=user_orders)
    else:
        # Initialize the form without any initial data for unauthenticated users
        contact_form = ContactQueryForm()

    # Process form submission
    if request.method == 'POST':
        contact_form = ContactQueryForm(request.POST, user_orders=user_orders)
        if contact_form.is_valid():
            contact_form.save()
            return redirect('contact_success')
        else:
            print(contact_form.errors)
            messages.error(request, 'Failed to send contact query. Please ensure the form is valid.')

    # Render the contact page with the form and user orders
    context = {
        'contact_form': contact_form,
        'user_orders': user_orders,
    }
    return render(request, 'contact/contact.html', context)



def contact_success(request):
    """
    A view to render the success page once the user submits the contact form.
    """
    return render(request, 'contact/contact_success.html')