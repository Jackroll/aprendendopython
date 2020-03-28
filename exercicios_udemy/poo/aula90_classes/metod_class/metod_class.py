

class Pessoa:
    ano_atual = 2020                                        #atributo de classe, pode ser acessado por qualquer método, inclusive o de classe

    def __init__(self, nome, idade):                        #atributo do método, acessível apenas aos métodos do objetos
        self.nome = nome
        self.idade = idade
        print(nome, idade)

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):          #método de classe, tyem acesso apenas aos atributos que não são de outros métodos, ou seja que são de classe
        idade = cls.ano_atual - ano_nascimento
        print(nome, idade)

#instanciando os objetos tipo Pessoa
p1 = Pessoa.por_ano_nascimento('Pedro', 1915)                   #acessando o método de classe
p1 = Pessoa('Jacson', 33)                                       #acessando o método do objeto
    