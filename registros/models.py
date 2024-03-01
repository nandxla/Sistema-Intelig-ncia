from django.db import models

# Create your models here.
class Fornecedor(models.Model):
    titular_choices = {
        "PF": "Conta PF",
        "PJ": "Conta PJ",
    }
    conta_choices = {
        "COR": "Corrente",
        "POU": "Poupança",
    }
    
    cnpj_cpf = models.CharField(max_length=20)
    razao_social = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    tipo_titular = models.CharField(max_length=100)
    tipo_titular = models.CharField(
        choices=titular_choices, 
        max_length=10,
        default="PJ",
    )
    tipo_conta = models.CharField(
        choices=conta_choices,
        max_length=10,
        default="COR"
    )
    
    def __str__(self) -> str:
        return self.cnpj_cpf
