# Generated by Django 4.2.6 on 2023-11-09 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('usuario', models.CharField(blank=True, max_length=10, null=True)),
                ('foto_logo', models.CharField(blank=True, max_length=100, null=True)),
                ('senha', models.IntegerField(blank=True, null=True)),
                ('data_nascimento', models.DateField(blank=True, null=True)),
                ('data_abertura', models.DateField(blank=True, null=True)),
                ('rg', models.CharField(blank=True, max_length=15, null=True)),
                ('cpf_cnpj', models.CharField(blank=True, max_length=15, null=True)),
                ('cliente_tipo', models.CharField(blank=True, choices=[['pessoa_física', 'pessoa_física'], ['pessoa_jurídica', 'pessoa_jurídica']], max_length=47, null=True)),
                ('cep', models.CharField(blank=True, max_length=10, null=True)),
                ('numero', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('saldo', models.FloatField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'CLientes',
            },
        ),
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('juros', models.DecimalField(decimal_places=2, max_digits=20)),
                ('numero_parcela', models.IntegerField()),
                ('valor_solicitado', models.DecimalField(decimal_places=2, max_digits=20)),
                ('Codigo_Cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cliente')),
            ],
            options={
                'verbose_name': 'Emprestimo',
                'verbose_name_plural': 'Emprestimos',
            },
        ),
        migrations.CreateModel(
            name='Movimentacao',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('operacao', models.CharField(max_length=1)),
                ('data_Hora', models.DateTimeField(auto_now=True)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=20)),
                ('Codigo_Cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cliente')),
            ],
            options={
                'verbose_name': 'Movimentação',
                'verbose_name_plural': 'Movimentações',
            },
        ),
        migrations.CreateModel(
            name='Investimento',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('grauRisco', models.CharField(max_length=5)),
                ('rentabilidade', models.DecimalField(decimal_places=2, max_digits=20)),
                ('Codigo_Cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cliente')),
            ],
            options={
                'verbose_name': 'Investimento',
                'verbose_name_plural': 'Investimentos',
            },
        ),
        migrations.CreateModel(
            name='EmprestimoParcela',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('data_vencimento', models.DateField()),
                ('valor_parcela', models.DecimalField(decimal_places=2, max_digits=20)),
                ('pago', models.BooleanField()),
                ('Codigo_Emprestimo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.emprestimo')),
            ],
            options={
                'verbose_name': 'Parcela',
                'verbose_name_plural': 'Parcelas',
            },
        ),
        migrations.CreateModel(
            name='Cartao',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('bandeira', models.CharField(max_length=20)),
                ('validade', models.DateField()),
                ('Codigo_Cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cliente')),
            ],
            options={
                'verbose_name': 'Cartao',
                'verbose_name_plural': 'Cartões',
            },
        ),
    ]
