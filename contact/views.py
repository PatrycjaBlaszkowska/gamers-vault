from django.shortcuts import render
from .forms import ContactQueryForm
from checkout.models import Order
from profiles.models import UserProfile  

def contact(request):
    """ A view to return the contact page with a form """  
    user_orders = None
    if request.user.is_authenticated:
        user_profile = UserProfile.objects.get(user=request.user)
        user_orders = Order.objects.filter(user_profile=user_profile)

    contact_form = ContactQueryForm(user_orders=user_orders)

    if request.method == 'POST':
        contact_form = ContactQueryForm(request.POST, user_orders=user_orders)
        if contact_form.is_valid():
            contact_form.save()

    context = {
        'contact_form': contact_form,
        'user_orders': user_orders,  
    }

    return render(request, 'contact/contact.html', context)
