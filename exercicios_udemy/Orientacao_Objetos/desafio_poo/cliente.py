"""
Sistema bancario:
     - Banco
        - Clientes
            - contas

        - Clientes:
        - tem que ter conta (corrente ou poupança)
        - Sacar
        - Depositar

    - Conta Corrente / Poupança :
        - Limite extra (pode ser sacado e ficar com saldo negativo)

    - Banco:
        - clientes
         - contas
"""
#Usado Herança, classe Cliente herda da Superclasse Pessoa
#Usado encapsulamento, nos atributos padrões da classe Pessoa, criado os getters
#Super classe Pessoa, com atributos padrão encapsulados
class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    #Fazendo getters
    @property
    def nome(self):
        return self._nome

    # Fazendo getters
    @property
    def idade(self):
        return self._idade


#Classe Cliente que herda da Superclasse Pessoa,
class Cliente (Pessoa):
    def __init__(self, nome, idade):            #sobrescrição do metodo init e atributos iniciais e cria o atributo conta
        super().__init__(nome, idade)
        self.conta = None

    #método que inclui uma conta para um determinado cliente
    def inserir_conta(self, conta):
        self.conta = conta








