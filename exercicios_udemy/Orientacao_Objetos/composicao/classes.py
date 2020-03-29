
#classe cliente que recebe uma instancia da classe endereço para atualizar sua lista de endereços
class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def insere_endereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))         #neste ponto é feita a composição, quando uma instancia da classe Endereço é chamada

    def lista_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)             #neste ponto tambem é feita a composição através do acesso aos atributos padrão
                                                                #atraves do instaciamento da classe Endereco()


#classe endereço,recebe dois atributos padrão
class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado
