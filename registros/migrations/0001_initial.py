# Generated by Django 5.0.2 on 2024-03-01 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj_cpf', models.CharField(max_length=20)),
                ('razao_social', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=100)),
                ('tipo_titular', models.CharField(choices=[('PF', 'Conta PF'), ('PJ', 'Conta PJ')], default='PJ', max_length=10)),
                ('tipo_conta', models.CharField(choices=[('COR', 'Corrente'), ('POU', 'Poupança')], default='COR', max_length=10)),
            ],
        ),
    ]
