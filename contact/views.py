from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactQueryForm
from checkout.models import Order
from profiles.models import UserProfile  

from django.core.mail import send_mail
from django.conf import settings

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
            # Save the form
            contact_query = contact_form.save()

            # Get form data
            user_name = contact_form.cleaned_data['name']
            user_email = contact_form.cleaned_data['email']
            query_type = contact_form.cleaned_data['query_type']
            message = contact_form.cleaned_data['message']

            # Send email to the site admin
            subject_admin = f"New Contact Query from {user_name}"
            message_admin = (
                f"Query Type: {query_type}\n"
                f"Message:\n{message}\n\n"
                f"User Email: {user_email}"
            )
            admin_email = 'gamers-vault@gmail.com'
            send_mail(subject_admin, message_admin, admin_email, [admin_email])

            # Send confirmation email to the user
            subject_user = "Thank you for contacting us"
            message_user = (
                f"Hi {user_name},\n\n"
                "Thank you for reaching out to us. We have received your query and will "
                "get back to you as soon as possible.\n\n"
                "Here’s a summary of your query:\n"
                f"Query Type: {query_type}\n"
                f"Message:\n{message}\n\n"
                "Best regards,\n"
                "The Gamer's Vault Support Team"
            )
            send_mail(subject_user, message_user, admin_email, [user_email])

            # Redirect to a success page
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