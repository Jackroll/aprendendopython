"""
Sistema bancario:
     - Banco
        - Clientes
            - contas
        Banco = [ [Clientes ] ]
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

from Orientacao_Objetos.desafio_poo.cliente import Cliente
from Orientacao_Objetos.desafio_poo.conta import ContaCorrente, ContaPoupanca
from Orientacao_Objetos.desafio_poo.banco import Banco

# instancia a classe Banco()
banco = Banco()

#Cria vários clientes através da classe Clientes ()
cliente01 = Cliente('Jacson', 33)
cliente02 = Cliente('Pedro', 54)
cliente03 = Cliente('Ivan ', 18)

#Cria varias contas com as classes ContaPoupança() e ContaCorrente()
conta01 = ContaPoupanca(568, 3035, 0)
conta02 = ContaCorrente(222, 3036, 0)
conta03 = ContaPoupanca(333, 3037, 0)

#Cadastra conta no banco atraves do método cadastrar_conta e Objeto banco
banco.cadastrar_conta(conta01)
banco.cadastrar_conta(conta02)
banco.cadastrar_conta(conta03)

# Cadastra cliente no banco atraves do método cadastrar_cliente e Objeto banco
banco.cadastrar_cliente(cliente01)
banco.cadastrar_cliente(cliente02)
banco.cadastrar_cliente(cliente03)

# Insere conta criada ao cliente especifico
cliente01.inserir_conta(conta01)
cliente02.inserir_conta(conta02)
cliente03.inserir_conta(conta03)

# Faz validação, verifica se a agencia, conta e cliente existem no banco
if banco.validacao(cliente02):
    cliente02.conta.deposito(500)
    cliente02.conta.sacar(550)
else:
    print('Não Autenticado')

if banco.validacao(cliente01):
    cliente01.conta.deposito(500)
    cliente01.conta.sacar(100)
else:
    print('Não Autenticado')