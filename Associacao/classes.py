

class Escritor:                                 #Criado classe Escritor
    def __init__(self, nome):                   #Atributos de instancia
        self.__nome = nome                      #Criado um atributo nome de modo Private __nome, para ser acessado fora da classe deve ser usado Getter and Setter
        self.__ferramenta = None                #Atributo será utilizado para possibilitar a associação entre as classes, ver associação no main.py

    @property                                   #Decorator para a criação do Getter
    def nome(self):                             #Criado o Getter nome, para pegar o atributo __nome, o atributo de instancia já serviu de Setter, por isso não precisou cria-lo
        return self.__nome

    @property                                   #Criação do getter do atributro de instancia Ferramenta
    def ferramenta(self):
        return self.__ferramenta

    @ferramenta.setter                          #Criado o Setter do atributo ferramenta, como ele não encontra-se inicializado no metodo __init__, deve ser criado o setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta


class Caneta:
    def __init__(self, marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

    def escrever(self):
        print('Caneta esta escrevendo...')

class MaquinaDeEscrever:
    def escrever(self):
        print('Maquina esta escrevendo...')