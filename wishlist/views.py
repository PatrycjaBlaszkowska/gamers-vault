from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Wishlist
from products.models import Product


@login_required
def wishlist_view(request):
    # Get all the wishlist items for the current logged-in user
    wishlist_items = Wishlist.objects.filter(user=request.user).select_related('product')
    
    context = {
        'wishlist_items': wishlist_items,
    }

    return render(request, 'wishlist/wishlist.html', context)

@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    Wishlist.objects.get_or_create(user=request.user, product=product)
    
    return redirect('products')