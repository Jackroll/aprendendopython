

class Escritor:
    def __init__(self, nome):
        self.__nome = nome
        self.__ferramenta = None                        #atributo preparado para receber qualquer valor, é o que vai proporcionar a associação

    #Getter para possibilitar acessar o atributo
    @property
    def ferramenta(self):
        return self.__ferramenta

    #Setter
    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta

    #Getter para possibilitar acessar o atributo
    @property
    def nome(self):
        return self.__nome


class Caneta:
    def __init__(self, marca):
        self.__marca = marca

    #Getter para possibilitar acessar o atributo
    @property
    def marca(self):
        return self.__marca

    def escrever(self):
        print('Escrevendo com a caneta')

class MaquinaDeEscrever:
    def escrever(self):
        print('Escrevendo com a máquina')
