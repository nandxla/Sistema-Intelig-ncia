from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('home_app.urls'), name='home'),
    path('registros/', include('registros.urls'), name='registros'),
    path('admin/', admin.site.urls),
]
