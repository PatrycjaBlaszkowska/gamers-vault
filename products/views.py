from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, Subcategory

def all_products(request):
    """ A view to show all products, including sorting and searching queries. """
    
    products = Product.objects.all()
    query = None
    categories = Category.objects.all()  
    subcategories = Subcategory.objects.all()
    sort = None
    direction = None

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
    
    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'categories': categories,  
        'subcategories': subcategories,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)

def product_details(request, product_id):
    """ A view to show individual product details. """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product' : product,
    }

    return render(request, 'products/product_details.html', context)


