import random

class Pessoa:
    ano_atual = 2020                                        #atributo de classe, pode ser acessado por qualquer método, inclusive o de classe

    #método de instancia, tem que receber o parametro self
    def __init__(self, nome, idade):                        #atributo do método, acessível apenas aos métodos do objetos
        self.nome = nome
        self.idade = idade
        print(nome, idade)

    #método de classe, precisa do parametro cls acessa somente os atributos de classe
    @classmethod                                                #decorador para definir que trata-se de classe de método
    def por_ano_nascimento(cls, nome, ano_nascimento):          #método de classe, tyem acesso apenas aos atributos que não são de outros métodos, ou seja que são de classe
        idade = cls.ano_atual - ano_nascimento
        print (nome, idade)

    #não pode ser usado o atributo self nem o cls
    #é metodo comum que não tem nada haver com a classe pessoa mas como esta dentro da classe pode ser acessada pela intancia ou pela classe
    #se este método não estivesse dentro da classe não daria de usar pelo objeto, é questão de organização
    @staticmethod                                           
    def gera_id():
        id = random.randint(10000, 19999)
        print(id)
    



#instanciando os objetos tipo Pessoa
p1 = Pessoa.por_ano_nascimento('Pedro', 1915)                   #acessando o método de classe
p1 = Pessoa('Jacson', 33)                                       #acessando o método do objeto
Pessoa.gera_id()                                                #static method pode ser chamado pela classe    
p1.gera_id()                                                    #static method pode ser chamado pela instancia

