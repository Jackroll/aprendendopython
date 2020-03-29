
#Classe pai - ou Super classe, as subclasses ou classes filhas herdam seus atributos e métodos
#Super Classes não herdam de subclasses
class Pessoa:
    def __init__ (self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self, nome):
        print(self.nome + ' Falando (super Classe) ...')

#SubClasse Cliente herdando os atributos da classe Pessoa
class Cliente(Pessoa):
    def comprar(self):                                              #as subclasses tambem podem ter seus próprios métodos ou atributos
        print (self.nome + ' Comprando ...')
    
    def falar(self, nome):
        print(self.nome + ' Falando estou no Cliente (Sub Classe) ...')

class ClienteVip(Cliente):                                                      #classe herdando de subclasse cliente()
    def falar(self, nome):                                                      #sobrescrevendo método falar() da super classe
        super().falar(nome)                                                     #executando primeiro o método da superclasse e depois da subclasse Sobrescrita
        print(self.nome + ' Falando Outra coisa método sobrescrito')            #Sebrescrevendo o método da super classe

#SubClasse Aluno herdando os atributos da classe Pessoa
class Aluno(Pessoa):
    def estudar(self):                                              #as subclasses tambem podem ter seus próprios métodos ou atributos
        print (self.nome + ' Estudando ...')

class ClienteVip2(Cliente):
    def __init__(self, nome, idade, sobrenome):                             #Sobrescrevendo os atributos iniciais da classe e incluindo o atributo sobrenome
        Pessoa.__init__(self, nome, idade)                                  #mantendo os atributos originais da super classe
        self.sobrenome = sobrenome                                          #atribuindo o novo atributo para a variável

    def falar(self, nome):
        Pessoa.falar(self, nome)                                            #pode ser chamado o método da super classe, incluindo o nome da classe na frente
        Cliente.falar(self, nome)                                           #pode ser chamado o método da super classe, incluindo o nome da classe na frente
        print(self.nome + ' Cliente vip 2 metodo sobrescrito')

    