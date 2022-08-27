from django.forms import ModelForm
from autenticacao.models import Cliente, Veiculo, Produto, Protocolo, Servico

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente 
        fields = ['nome', 'cpf', 'data_nascimento','telefone','email']

class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['nome_produto', 'preco', 'descricao']