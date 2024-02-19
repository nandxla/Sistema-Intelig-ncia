from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_registros),
    path('fornecedor/', views.registro_fornecedor),
]
