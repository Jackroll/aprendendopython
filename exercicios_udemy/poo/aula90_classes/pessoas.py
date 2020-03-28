from datetime import datetime

class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))                #atributo de classe

    def __init__(self, nome, idade, comendo = False, falando=False):        #atributo do objeto, o de método
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def falar(self, assunto): 
        if self.comendo:
            print(f'{self.nome} esta comendo não pode falar')
            return
        
        if self.falando:
            print(f'{self.nome} já esta falando')
            return

        print(f'{self.nome} esta falando sobre {assunto}')
        self.falando = True

    def comer(self, alimento):
        if self.falando:
            print(f'{self.nome} esta falando não pode comer')
            return

        if self.comendo:
            print(f'{self.nome} já esta comendo')
            return

        print(f'{self.nome} esta comendo {alimento}')
        self.comendo = True

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} já não esta falando')
            return
        print(f'{self.nome} parou de falar')
        self.falando = False

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} já não esta comendo')
            return
        print(f'{self.nome} parou de comer')
        self.comendo = False

    def ano_nascimento(self):
        ano = self.ano_atual - self.idade
        print(f'{self.nome} nasceu em {ano}')

        