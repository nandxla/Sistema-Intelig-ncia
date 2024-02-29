from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_registros, name='registros-home'),
    path('fornecedor/', views.registro_fornecedor, name='registros-fornecedor'),
]
