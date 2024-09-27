from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactQueryForm
from .models import UserProfile, Order

def contact(request):
    """ 
    A view to return the contact page with a form.
    Authenticated users can see their previous orders.
    """
    user_orders = get_user_orders(request)
    contact_form = initialize_contact_form(request, user_orders)

    if request.method == 'POST':
        if process_contact_form(request, contact_form):
            # Sending email after form is valid and saved
            send_contact_email(contact_form.cleaned_data)
            return redirect('contact_success')
        else:
            messages.error(request, 'Failed to send contact query. Please ensure the form is valid.')

    return render_contact_page(request, contact_form, user_orders)


def get_user_orders(request):
    """
    Get the authenticated user's orders if they exist.
    Returns None if the user is not authenticated or has no orders.
    """
    if request.user.is_authenticated:
        try:
            user_profile = UserProfile.objects.get(user=request.user)
            return Order.objects.filter(user_profile=user_profile)
        except UserProfile.DoesNotExist:
            return None
    return None


def initialize_contact_form(request, user_orders):
    """
    Initialize the contact form with or without POST data based on the request method.
    Pass user orders if available.
    """
    if request.method == 'POST':
        return ContactQueryForm(request.POST, user_orders=user_orders)
    return ContactQueryForm(user_orders=user_orders)


def process_contact_form(request, contact_form):
    """
    Validate and process the contact form submission.
    Returns True if the form is valid and saved, False otherwise.
    """
    if contact_form.is_valid():
        contact_form.save()
        return True
    return False


def send_contact_email(form_data):
    """
    Send two emails:
    1. One to the site administrator/support team.
    2. One to the customer who submitted the contact form.
    """
    # Email to the support team
    subject_admin = f"New Contact Query ({form_data['query_type']})"
    message_admin = (
        f"Name: {form_data['name']}\n"
        f"Email: {form_data['email']}\n"
        f"Query Type: {form_data['query_type']}\n"
        f"Message: {form_data['message']}\n"
    )
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list_admin = [settings.DEFAULT_FROM_EMAIL]  # Replace with your support email

    # Send email to admin/support
    send_mail(
        subject_admin,
        message_admin,
        from_email,
        recipient_list_admin,
        fail_silently=False,
    )

    # Email confirmation to the customer
    subject_customer = "Thank you for contacting us"
    message_customer = (
        f"Dear {form_data['name']},\n\n"
        f"Thank you for reaching out to us with your {form_data['query_type']} query. "
        f"We have received your message and will get back to you as soon as possible.\n\n"
        f"Here is a copy of your message:\n\n"
        f"{form_data['message']}\n\n"
        f"Best regards,\nThe Support Team"
    )
    recipient_list_customer = [form_data['email']]  # Send email to the customer

    # Send confirmation email to customer
    send_mail(
        subject_customer,
        message_customer,
        from_email,
        recipient_list_customer,
        fail_silently=False,
    )


def render_contact_page(request, contact_form, user_orders):
    """
    Render the contact page with the form and user orders in the context.
    """
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
