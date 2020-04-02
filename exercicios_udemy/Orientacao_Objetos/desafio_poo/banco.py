
# Classe Banco, possui cadastro com agencias, clientes e contas
class Banco:
    def __init__(self):
        self.agencia = [111, 222, 333]
        self.clientes = []
        self.contas = []

    #método para cadastrar clientes no banco
    def cadastrar_cliente(self, cliente):
        self.clientes.append(cliente)

    #método para cadastrar conta no banco
    def cadastrar_conta(self, conta):
        self.contas.append(conta)

    #método para autenticação, somente será possível fazer transações se o cliente, a cota e a agencia existirem no banco
    #ou seja se já tiverem sido cadastrados
    def validacao(self, cliente):
        if cliente not in self.clientes:
            return False
        if cliente.conta not in self.contas:
            return False
        if cliente.conta.agencia not in self.agencia:
            return False
        return True