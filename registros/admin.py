from django.contrib import admin
from . import models

# Register your models here.
class FornecedorAdmin(admin.ModelAdmin):
    ...
    
admin.site.register(
    models.Fornecedor,  # registrando model
    FornecedorAdmin,    # registrando modelAdmin 
)