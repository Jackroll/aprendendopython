from classes.conta import Conta

#Classe filha da super classe abstrata Conta, somente pode ser instanciada após a criação
#do método abstrato obrigatório
class ContaPoupanca(Conta):
    def sacar(self, valor):                                                     #Polimorfismo, classe abstrata definida para a classe poder ser instanciada
        if valor > self._saldo:
            print("Não existe saldo suficiente para o saque solicitado")
            return
        if not isinstance(valor, (int, float)):
            raise ValueError("Valor de saque precisa ser numérico")
        
        self.saldo -= valor
        self.detalhes()