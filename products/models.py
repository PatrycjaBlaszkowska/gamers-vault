from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Subcategory(models.Model):

    class Meta:
        verbose_name_plural = 'Subcategories'

    # Subcategories related to a parent category
    category = models.ForeignKey(
        'Category', related_name='subcategories', on_delete=models.CASCADE
    )
    name = models.CharField(max_length=254)

    def __str__(self):
        return f"{self.category.name} - {self.name}"


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL
    )
    subcategory = models.ForeignKey(
        'Subcategory', null=True, blank=True, on_delete=models.SET_NULL
    )
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True
    )
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)


def __str__(self):
    return self.name


class ProductReview(models.Model):
    product = models.ForeignKey(
        Product, related_name='reviews',
        null=True, blank=True,
        on_delete=models.SET_NULL
    )
    user = models.ForeignKey(
        User, null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    title = models.CharField(max_length=254)
    rating = models.PositiveIntegerField()
    content = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} - {self.title}"

    class Meta:
        ordering = ['-added_on']
