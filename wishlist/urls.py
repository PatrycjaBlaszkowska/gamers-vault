from django.urls import path
from . import views

urlpatterns = [
    path('wishlist/', views.wishlist_view, name='wishlist'),
]