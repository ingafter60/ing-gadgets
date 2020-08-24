# project/urls.py
from django.contrib import admin
from django.urls import path

from apps.cart.views import cart
from apps.core.views import frontpage, contact, about
from apps.store.views import product_detail, category_detail

urlpatterns = [
	path('', frontpage, name='frontpage'),
   path('cart/', cart, name='cart'),
	path('contact/', contact, name='contact'),
   path('about/', about, name='about'),
   path('admin/', admin.site.urls),   
   path('<slug:category_slug>/<slug:slug>/', product_detail, name='product_detail'),
   path('<slug:slug>/', category_detail, name='category_detail'),

]

