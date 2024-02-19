from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('registros.urls')),
    path('admin/', admin.site.urls),
]
