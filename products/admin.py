from django.contrib import admin
from .models import Product, Category, Subcategory, ProductReview

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'subcategory',
        'price',
        'rating',
        'image',
    )

    ordering = ('category',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
class SubcategoryAdmin(admin.ModelAdmin):
        list_display = (
        'name',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(ProductReview)