from abc import ABC, abstractmethod # para poder criar a classe abstrata

#classe abstrata Conta, trata-se de um conceito geral
#não pode ser instanciada, apenas sua classe filha, especializada, como por exemplo a classe ContaPoupanca()
class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    @property
    def agencia(self):
        return self._agencia

    @property
    def conta(self):
        return self._conta

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("Saldo precisa ser numérico")

        self._saldo = valor

    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("Valor de depósito precisa ser numérico")
        
        self.saldo += valor
        self.detalhes()
        
    def detalhes(self):
        print(f'Agência : {self._agencia} | ', end = '')
        print(f'Conta : {self._conta} | ', end = '')
        print(f'Saldo : {self._saldo} ')

    # método abstrato, sem instanciar esse método,  a classe filha (especializada) não consegue funcionar
    # deste modo é forçado a classe espcializada a criar o método, conforme visto na classe ContaPoupanca()
    # o método não precisa executar nenhuma ação, apenas existir
    @abstractmethod
    def sacar(self, valor):
        pass
