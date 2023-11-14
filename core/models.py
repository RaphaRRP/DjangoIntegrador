from django.db import models

def upload_image(instance, filename):
    return f'{instance.codigo}-{filename}'

class Cliente(models.Model):

    #ID
    codigo = models.AutoField(primary_key=True) 
    #...
    usuario = models.CharField(max_length=10, null=True, blank=True)
    senha = models.IntegerField(null=True, blank=True)
    data_abertura = models.DateField(null=True, blank=True, auto_now_add=True)
    cpf_cnpj = models.CharField(max_length=15, null=True, blank=True)
    cep = models.CharField(max_length=10, null=True, blank=True)
    numero = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    saldo = models.FloatField(null=True, blank=True)
    emprestimo = models.FloatField(default=0, blank=True)
    cartao = models.BooleanField(default=False)
    image = models.ImageField(upload_to=upload_image, blank=True, null=True)


    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return str(self.pk)
    

class Movimentacao(models.Model):

    #ID
    codigo = models.AutoField(primary_key=True)  
    #...
    data_Hora = models.DateTimeField(auto_now=True)
    valor = models.DecimalField(decimal_places=2, max_digits=20)
    #FK
    cliente_pagar = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='movimentacao_cliente_pagar')
    cliente_receber = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='movimentacao_cliente_receber')

    class Meta:
        verbose_name = 'Movimentação'
        verbose_name_plural = 'Movimentações'

    def __str__(self):
        return str(self.pk)


class Investimento(models.Model):

    #ID
    codigo = models.AutoField(primary_key=True) 
    #...
    grauRisco = models.CharField(max_length=5)#choice
    rentabilidade = models.DecimalField(decimal_places=2, max_digits=20)
    #FK
    Codigo_Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Investimento'
        verbose_name_plural = 'Investimentos'

    def __str__(self):
        return str(self.pk)

    
class Emprestimo(models.Model):

    #ID
    codigo = models.AutoField(primary_key=True) 
    #...
    valor_solicitado = models.DecimalField(decimal_places=2, max_digits=20)
    #FK
    Codigo_Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='emprestimo_cliente')

    class Meta:
        verbose_name = 'Emprestimo'
        verbose_name_plural = 'Emprestimos'

    def __str__(self):
        return str(self.pk)

