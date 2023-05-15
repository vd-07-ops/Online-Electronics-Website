
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HOME, name='home'),
    path('base/',views.BASE, name='base'),
    path('products/',views.PRODUCT, name="products"),
    path('search/',views.SEARCH, name="search"),
    path('products/<str:id>',views.PRODUCT_DETAIL_PAGE,name="product_details"),
    path('contact/', views.CONTACT_PAGE, name='contact')

] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
