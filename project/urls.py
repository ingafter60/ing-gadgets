# project/urls.py
from django.contrib import admin
from django.urls import path

from apps.core.views import helloworld

urlpatterns = [
	path('', helloworld, name='helloworld'),
   path('admin/', admin.site.urls),
]
