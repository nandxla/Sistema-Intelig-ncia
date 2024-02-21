from django import forms

class FornecedorForm(forms.Form):
    tipo_titular_campos = [
        (1, "Conta PF"),
        (2, "Conta PJ")
    ]
    
    tipo_conta_campos = [
        (1, "Corrente"),
        (1, "Poupança"),
    ]
    
    cnpj_cpf = forms.CharField(label="CNPJ ou CPF", max_length=150)
    razao_social = forms.CharField(label="Razão Social", max_length=150)
    telefone = forms.CharField(label="Telefone", max_length=150)
    email = forms.CharField(label="Email", max_length=150)
    tipo_titular = forms.ChoiceField(label="Tipo de Titular", choices=tipo_titular_campos)
    tipo_conta = forms.ChoiceField(label="Tipo de Conta", choices=tipo_conta_campos)
    banco = forms.CharField(label="Banco", max_length=150)
    agencia = forms.CharField(label="Agencia", max_length=150)
    conta = forms.CharField(label="conta", max_length=150)
