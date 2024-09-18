from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Wishlist

@login_required 
def wishlist_view(request):
    # Get all the wishlist items for the current logged-in user
    wishlist_items = Wishlist.objects.filter(user=request.user).select_related('product')
    
    template = 'wishlist/wishlist.html'
    context = {
        'wishlist_items': wishlist_items,
    }

    return render(request, template, context)