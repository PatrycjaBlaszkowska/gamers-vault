from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from gamers_vault import views as gamers_vault_views
from django.conf.urls import handler404, handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    path('bag/', include('bag.urls')),
    path('checkout/', include('checkout.urls')),
    path('profile/', include('profiles.urls')),
    path('wishlist/', include('wishlist.urls')),
    path('contact/', include('contact.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Custom error handlers
handler404 = gamers_vault_views.error_404
handler500 = gamers_vault_views.error_500
