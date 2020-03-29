"""Composição:
Uma classe é dona de objetos de outra classe
Se a classe principal for apagada todas as classes que foram usadas pela classe principal serão apgadas com ela

"""

#Por conta da composição, não houve a necessidad de importação da classe endereço, já que ela compoe a classe Cliente
from classes import Cliente

print('-='*15)
c1 = Cliente('Jacson', 33)
c1.insere_endereco('Imarui', 'SC')
c1.lista_enderecos()

print('-='*15)
c2 = Cliente('Pedro', 12)
c2.insere_endereco('Londrina', 'PR')
c2.lista_enderecos()

print('-='*15)
c3 = Cliente('Bia', 43)
c3.insere_endereco('Salvador', 'BA')
c3.insere_endereco('Belem', 'PA')
c3.lista_enderecos()

print('-='*15)