from .models import Category, Subcategory

def categories_and_subcategories(request):
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()

    return {
        'categories': categories,
        'subcategories': subcategories,
    }