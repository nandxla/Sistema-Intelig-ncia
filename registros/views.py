from django.shortcuts import render
from .forms import (
    FornecedorForm,
)

def home_registros(request):
    return render(request, 'registros/pages/index.html')

def registro_fornecedor(request):
    
    form_fornecedor = FornecedorForm()
    return render(
        request, 
        'registros/pages/registro_fornecedor.html',
        context={
            "form_fornecedor": form_fornecedor,
        }
    )
