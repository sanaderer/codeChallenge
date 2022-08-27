from django.forms import ModelForm
from app.models import Cliente, Veiculo, Produto, Protocolo, Servico

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente 
        fields = ['nome', 'cpf', 'data_nascimento','telefone','email']