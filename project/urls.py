# project/urls.py
from django.contrib import admin
from django.urls import path

from apps.core.views import frontpage, contact
from apps.store.views import product_detail

urlpatterns = [
	path('', frontpage, name='frontpage'),
	path('contact/', contact, name='contact'),
   path('<slug:slug>/', product_detail, name='product_detail'),
   path('admin/', admin.site.urls),
]
