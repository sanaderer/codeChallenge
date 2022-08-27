from django.contrib import admin
from .models import Cliente, Veiculo, Produto, Servico

# Register your models here.
@admin.register(Cliente)
class Cliente(admin.ModelAdmin):
    list_display = ['nome', 'cpf', 'data_nascimento', 'telefone', 'email']
    list_filter = ['nome', 'cpf']
    search_fields = ['nome']

admin.site.register(Veiculo)
admin.site.register(Produto)
admin.site.register(Servico)
