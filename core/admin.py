from django.contrib import admin

from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = [
            'codigo', 'usuario', 'foto_logo', 'senha', 'data_nascimento', 'data_abertura', 'nome_razaoSocial', 'nomeSocial_fantasia', 'cnpj','inscricao_estadual', 'inscricao_municipal', 'rg', 'cpf', 'cliente_tipo'
        ]