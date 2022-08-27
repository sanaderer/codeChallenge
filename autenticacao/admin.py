from django.contrib import admin
from .models import Cliente, Veiculo, Produto, Servico

# Register your models here.
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cpf', 'data_nascimento', 'telefone', 'email', 'numero_protocolo']
    list_filter = ['nome', 'cpf']
    search_fields = ['nome', 'protocolo']

