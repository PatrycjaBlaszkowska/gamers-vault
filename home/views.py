from django.shortcuts import render
from products.models import Category, Subcategory

def index(request):
    """ A view to return home page. """

    return render(request, 'home/index.html')
