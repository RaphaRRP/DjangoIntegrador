from django.db import models


class Cliente(models.Model):

    #ID
    codigo = models.AutoField(primary_key=True) 

    #...
    usuario = models.CharField(max_length=10)
    foto_logo = models.CharField(max_length=100)
    senha = models.IntegerField()
    data_nascimento = models.DateField()
    data_abertura = models.DateField()
    nome_razaoSocial = models.CharField(max_length=100)
    nomeSocial_fantasia = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=15)
    inscricao_estadual = models.CharField(max_length=100)
    inscricao_municipal = models.CharField(max_length=100)
    rg = models.CharField(max_length=15)
    cpf = models.CharField(max_length=15)
    cliente_tipo = models.IntegerField()#choice

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'CLientes'

    def __str__(self):
        return self.nomeSocial_fantasia


class Endereco(models.Model):
    
    #ID
    codigo = models.AutoField(primary_key=True) 

    #...
    bairro = models.CharField(max_length=100)
    logradouro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    cep = models.CharField(max_length=10)
    uf = models.CharField(max_length=2)

    #FK
    fk_codigo_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Endereco'
        verbose_name_plural = 'Enderecos'

    def __str__(self):
        return self.cep

    
class Contato(models.Model):

    #ID
    codigo = models.AutoField(primary_key=True) 

    #...
    observacao = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    ramal = models.CharField(max_length=10)
    numero = models.CharField(max_length=15)

    #FK
    fk_codigo_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'

    def __str__(self):
        return self.numero


class Conta(models.Model):

    #ID
    codigo = models.AutoField(primary_key=True) 

    #...
    agencia = models.CharField(max_length=10)
    numero = models.CharField(max_length=20)
    limite = models.IntegerField()
    tipo = models.CharField(max_length=100)  #choice
    ativa = models.BooleanField()

    #FK
    fk_codigo_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Conta'
        verbose_name_plural = 'Contas'

    def __str__(self):
        return self.numero

"""
class MantemClienteConta(models.Model):

    #FK
    fk_conta_codigo = models.ForeignKey(Conta)
    fk_cliente_codigo = models.ForeignKey(Cliente)
    fk_cliente_codigoCliente = models.ForeignKey(Cliente)
"""


class Cartao(models.Model):

    #ID
    codigo = models.AutoField(primary_key=True) 


    #...
    situacao = models.CharField(max_length=20)#choice
    bandeira = models.CharField(max_length=20)#choice
    numero = models.CharField(max_length=30)
    cvv = models.CharField(max_length=5)
    validade = models.DateField()

    #FK
    fk_codigo_conta = models.ForeignKey(Conta, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Cartao'
        verbose_name_plural = 'Cartões'

    def __str__(self):
        return self.numero
    


class Movimentacao(models.Model):

    #ID
    codigo = models.AutoField(primary_key=True)  

    #...
    operacao = models.CharField(max_length=1)#choice
    data_Hora = models.DateTimeField(auto_now=True)
    valor = models.DecimalField(decimal_places=2, max_digits=20)

    #FK
    fk_codigo_cartao = models.ForeignKey(Cartao, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Movimentação'
        verbose_name_plural = 'Movimentações'

    def __str__(self):
        return self.codigo



class Investimento(models.Model):

    #ID
    codigo = models.AutoField(primary_key=True) 

    #...
    grauRisco = models.CharField(max_length=5)#choice
    finalizado = models.BooleanField()
    rentabilidade = models.DecimalField(decimal_places=2, max_digits=20)
    aporte = models.DecimalField(decimal_places=2, max_digits=20)
    tipo = models.CharField(max_length=30)#choice
    prazo = models.CharField(max_length=20)
    taxa_administracao = models.DecimalField(decimal_places=2, max_digits=20)

    #FK
    fk_codigo_conta = models.ForeignKey(Conta, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Investimento'
        verbose_name_plural = 'Investimentos'

    def __str__(self):
        return self.codigo

    
class Emprestimo(models.Model):

    #ID
    codigo = models.AutoField(primary_key=True) 

    #...
    juros = models.DecimalField(decimal_places=2, max_digits=20)
    numero_parcela = models.IntegerField()
    data_solicitacao = models.DateField()
    data_aprovacao = models.DateField()
    aprovado = models.BooleanField()
    valor_solicitado = models.DecimalField(decimal_places=2, max_digits=20)
    observacao = models.CharField(max_length=200)

    #FK
    fk_codigo_conta = models.ForeignKey(Conta, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Emprestimo'
        verbose_name_plural = 'Emprestimos'

    def __str__(self):
        return self.codigo
    

class EmpretimoParcela(models.Model):

    #ID
    codigo = models.AutoField(primary_key=True) 


    #...
    data_vencimento = models.DateField()
    valor_parcela = models.DecimalField(decimal_places=2, max_digits=20)
    numero = models.IntegerField()
    data_pagamento = models.DateField()
    valor_pago = models.DecimalField(decimal_places=2, max_digits=20)

    #FK
    fk_codigo_emprestimo = models.ForeignKey(Emprestimo, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Parcela'
        verbose_name_plural = 'Parcelas'

    def __str__(self):
        return self.codigo














