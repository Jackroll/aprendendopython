"""Herança Multipla:
class A:
class B (A):
class C (B):
class D (B, C) --> Herança Multipla

Foram criadas 3 classes: Eletronico, SmartPhone e LogMixin
 - Eletronico é a super classe com atributos e métodos padrões
 - LogMixin é totalmente idependente das outras duas classes e não herda de nenhuma classe, é usada para trazer funcionalidade para classe que herda-la
 - SmartPhone herda de Eletronico e Logmixin
    Alem dos atributos e metodos padrões a classe SmartPhone, sobrescreveu adiconando atributos ao metodo __init__ de Eletronico
    Do logmixin herdou melhorias e funcionalidades
"""

from eletronico import Smartphone

s1 = Smartphone('S10')

s1.desligar()
s1.conectar()
s1.ligar()
s1.conectar()
s1.desconectar()
s1.desligar()
s1.desconectar()
s1.conectar()
s1.conectar()
s1.conectar()


