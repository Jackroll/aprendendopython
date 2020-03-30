from classes.conta import Conta

class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=100):                  #adicionando atributo ao metodo init da classse pai
        super().__init__(agencia, conta, saldo)                             #usado o super() ara manter os atributos originais
        self._limite = limite
    
    @property
    def limite(self):
        return self._limite

    def sacar(self, valor):                                                     #Polimorfismo classe abstrata definida para a classe poder ser instanciada
        if valor > (self._saldo + self._limite):
            print("Não existe saldo suficiente para o saque solicitado")
            return
        
        if not isinstance(valor, (int, float)):
            raise ValueError("Valor de saque precisa ser numérico")
        
        self.saldo -= valor
        self.detalhes()