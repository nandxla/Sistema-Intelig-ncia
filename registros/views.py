from django.shortcuts import render


def home_registros(request):
    return render(request, 'registros/index.html')

def registro_fornecedor(request):
    return render(request, 'registros/registro_fornecedor.html')
