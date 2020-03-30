"""classes abstratas (é um conceito)
Não pode ser instanciada, é força as subclasses a fazer alguma ação
deve ser sempre isntanciada a especialização da Classe abstrata

exemplo:
 - Conta Bancaria - Classe abstrata é um conceito - não pode ser instanciada
 - Conta Corrente, é uma especialização da classe abstrata Conta Bancaria
 - Conta Poupança
 - Conta Universitária, etc....

 Para pode fazer uma classe abstrata deve ser imporata a ABC e abstractmethod from abc

 Polimorfismo: é o prncipio que permite que classes derivadas de uma mesma superclasse
 tenham metodos iguais (mesma assinatura) mas comportamentos diferentes
 Mesma assinatura = mesma qtd e tipo de parametros
 Exemplo: metodo sacar, e um metodo abstrato na superclasse e é recriado nas classes
 cContaPoupança e ContaCorrente, que possui a mesma assinatura, no entanto funcionamento diferente
 pois na classe ContaCorrente foi adicionado limite
"""

from classes.contapoupanca import ContaPoupanca
from classes.contacorrente import ContaCorrente

print('Conta Poupança -=-=-=-=-=-=-=-=-=-=--=')
c1 = ContaPoupanca(55, 200, 2000)
c1.sacar(1000)
c1.depositar(10000)

print('Conta Corrente -=-=-=-=-=-=-=-=-=-=--=')
c2 = ContaCorrente(60, 300, 5000)
c2.sacar(5050)