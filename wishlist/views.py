from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Wishlist
from products.models import Product


@login_required
def wishlist_view(request):
    """ A view to see product on the user's wishlist """
    wishlist_items = Wishlist.objects.filter(
        user=request.user).select_related('product')

    context = {
        'wishlist_items': wishlist_items,
    }

    return render(request, 'wishlist/wishlist.html', context)


@login_required
def toggle_wishlist(request, product_id):
    """ Toggle the item in the wishlist
    (add if not present, remove if present) """

    try:
        product = get_object_or_404(
            Product,
            id=product_id
        )

        wishlist_item = Wishlist.objects.filter(
            user=request.user, product=product).first()

        if wishlist_item:
            wishlist_item.delete()
            message = f'Removed {product.name} from your wishlist.'
        else:
            Wishlist.objects.create(user=request.user, product=product)
            message = f'Added {product.name} to your wishlist.'

        messages.success(request, message)
        # Redirect back to the referring page or 'products' if no referrer
        return redirect(request.META.get('HTTP_REFERER', 'products'))
    except Exception as e:
        messages.error(request, f'Error toggling item: {e} in wishlist')
        return HttpResponse(status=500)
