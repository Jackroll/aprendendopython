"""
Associação - UM objetos Usa objetos de outra classe
Agregação - Um objeto Tem objetos de outra classe
Composição - Um objeto É dono de objetos de outras classes
Herança - Um objeto é outro objeto

Exemplo Herança:
Se eu tenho uma classe Cliente que possui atributos nome e idade, e outra classe Alunos que possui os atributos nome e idade tambem
percebe-se uma repetição de códigos desnecessários, pois ambos possuem os mesmos atributos, deste modo pode-se criar uma unica classe
Pessoas() com o atributos e ou métodos padrão que podem ser herdados pelas outras classes, deste modo estou afirmando que um Cliente() é uma pessoa e 
um Aluno()

Podem ser sobrescritos métodos da super classe, criando o mesmo método na subclasse, mas caso seja necessário ainda assim executar o método original (Super classe)
este pode ser chamado atraves do Super().nomemetodo(), ou ainda informando o nome da classe na frente NomeClasse().nomemetodo()
Se usar o Super().metodo(atributo) - deve passar o atributo se existir
Se usar o nome da classe NomeClasse().metodo(self, atributo) - deve passar o self e os atributos se existirem

Subclasses podem herdar de subclasses exemplo:
class Pai() - Super
class Filha(Pai) - Subclasse
class FilhaDaFilha(Filha) - Subclasse

A herança é exercida de cima pra baixo

"""

from classes import *

print('-='*30)
c1 = Cliente('Jacson', 33)
print(f'Classe : {c1.nomeclasse}')
print(c1.nome, c1.idade)
c1.comprar()
c1.falar(c1.nome)

print('-='*30) 
a1 = Aluno('Gustavo', 29)
print(f'Classe : {a1.nomeclasse}')
print(a1.nome, a1.idade)
a1.estudar()
a1.falar(a1.nome)

print('-='*30)
print('Sobrescrevendo o método da super classe, mas mostrando o método da super classe antes')
c2 = ClienteVip('JAcson', 33)
c2.falar(c2.nome)

print('-='*30)
c3 = ClienteVip2('Batista', 95, 'De Castro')
print(c3.nome, c3.sobrenome)
c3.falar(c3.nome)
print('-='*30)