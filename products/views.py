from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Avg, Case, When, Value, IntegerField
from django.db.models.functions import Lower

from .models import Product, Category, Subcategory, ProductReview
from wishlist.models import Wishlist
from .forms import ProductForm, ProductReviewForm

from django.db.models import Case, When, Value, IntegerField, F


def all_products(request):
    """ A view to show all products, including sorting and searching queries. """
    
    products = Product.objects.all()
    query = None
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    sort = None
    direction = None

    if request.user.is_authenticated:
        wishlist_items = Wishlist.objects.filter(user=request.user).values_list('product_id', flat=True)
        # Fetch user ratings for the products
        user_ratings = ProductReview.objects.filter(user=request.user).values('product_id', 'rating')
        user_ratings_dict = {item['product_id']: item['rating'] for item in user_ratings}
    else:
        wishlist_items = []
        user_ratings_dict = {}

    if request.GET:
        category_filter = request.GET.get('category', None)
        subcategory_filter = request.GET.get('subcategory', None)

        if category_filter:
            products = products.filter(category__name=category_filter)

        if subcategory_filter:
            products = products.filter(subcategory__name=subcategory_filter)

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'

        if 'direction' in request.GET:
            direction = request.GET['direction']
            if direction == 'desc':
                sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    # Annotate products with user rating if available
    products = products.annotate(
        user_rating=Case(
            *[When(id=pk, then=Value(rating)) for pk, rating in user_ratings_dict.items()],
            default=Value(0),
            output_field=IntegerField(),
        )
    )

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'categories': categories,
        'subcategories': subcategories,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'wishlist_items': wishlist_items,
        'user_ratings': user_ratings_dict,
    }

    return render(request, 'products/products.html', context)



def product_details(request, product_id):
    """ A view to show individual product details and reviews. """
    
    product = get_object_or_404(Product, pk=product_id)
    reviews = product.reviews.all()
    review_form = ProductReviewForm()

    if reviews.exists():
        average_rating = reviews.aggregate(Avg('rating'))['rating__avg']
    else:
        average_rating = product.rating

    context = {
        'product': product,
        'reviews': reviews,
        'average_rating': average_rating,
        'review_form': review_form,
    }

    return render(request, 'products/product_details.html', context)


@login_required
def add_product(request):
    """ A view to add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only storeowners can add new products.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product =  form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_details', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else: 
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ A view to edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only storeowners can edit products.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_details', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else: 
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ A view to delete the product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only storeowners can delete products.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Successfully deleted product!')
    return redirect(reverse('products'))


@login_required
def add_review(request, product_id):
    """ A view to add a product review. """

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        review_form = ProductReviewForm(request.POST)
        
        if review_form.is_valid():
            existing_review = ProductReview.objects.filter(product=product, user=request.user).first()

            if existing_review:
                messages.error(request, 'You have already reviewed this product.')
                return redirect('product_details', product_id=product.id)

            review = review_form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            messages.success(request, 'Your review has been added!')
            return redirect('product_details', product_id=product.id)
        else:
            messages.error(request, 'Failed to add review. Please ensure the form is valid.')

        review_form = ProductReviewForm()
        context = {
            'product': product,
            'review_form': review_form,
        }
        return render(request, 'products/product_details.html', context)