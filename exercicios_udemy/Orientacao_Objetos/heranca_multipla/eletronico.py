
from log import LogMixin

class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if self._ligado:
            return
        print(f'{self._nome} Ligou ')
        self._ligado = True
    
    def desligar(self):
        if not self._ligado:
            return
        self._ligado = False

#Herança multipla, herda da classe Eletronico e LogMixin
class Smartphone(Eletronico, LogMixin): 
    def __init__(self, nome):
        super().__init__(nome)
        self._conectado = False                     #sobrescrição dos atributos da classe e inclusão de atributo conectado

    def conectar(self):
        if not self._ligado:
            info = f'{self._nome} não esta ligado'
            print(info)
            self.log_info(info)                     #metodo da Classe LogMixin herdada
            return

        if self._conectado:
            error = f'{self._nome} já esta conectado'
            print(error)
            self.log_error(error)
            return

        info = f'{self._nome} conectou'
        print(info)
        self.log_info(info)
        self._conectado = True
        

    def desconectar(self):
        if not self._conectado:
            error = f'{self._nome} não esta conectado'
            print(error)
            self.log_error(error)
            return

        info = f'{self._nome} foi desconectado'
        print(info)
        self.log_info(info)
        self._conectado = False