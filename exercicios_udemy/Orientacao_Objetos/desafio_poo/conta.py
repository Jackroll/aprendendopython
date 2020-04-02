from abc import ABC, abstractmethod     #importação para usar abstração

#Usado Abstração na SuperClasse Conta e método sacar
# Usado herança, classes ContaPoupanca e ContaCorrente herdam sa superclasse Abstrata Conta()
# Classe abstrata Conta(), possui atributos padrões agencia, conta e saldo
class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    #método para efetuar o deposito, o valor é armazenado no saldo
    def deposito(self, valor):
        self.saldo += valor

    #método para mostrar os detalhes das contas, chamada sempre que é feito um depósito ou saque
    def detalhes(self):
        print(f'Agencia: {self.agencia} Conta: {self.conta} Saldo: {self.saldo}')

    #método abstrato, deve ser instanciado nas classes ContaPoupanca e ContaCorrente
    @abstractmethod
    def sacar(self, valor):
        pass

# Classe ContaPoupanca herda da Superclasse Conta, possui um método sacar
class ContaPoupanca(Conta):
    def sacar(self, valor):
        if valor > self.saldo:
            print('Saldo insuficiente')
            return
        self.saldo -= valor
        self.detalhes()

# Classe ContaCorrente herda da Superclasse Conta, possui um método sacar
class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=100):      #Sobrescrito os atributos da superclasse e adicionado atributo limite
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        if valor > self.saldo + self.limite:
            print('Saldo insuficiente')
            return
        self.saldo -= valor
        self.detalhes()