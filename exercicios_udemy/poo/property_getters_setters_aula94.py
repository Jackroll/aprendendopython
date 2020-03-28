

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def desconto(self, percentual):
        self.preco = self.preco  - (self.preco*(percentual/100))
        print(self.nome, self.preco)

    #exemplo legal: padronizar a formatação das palavras, com a primeira letra sempre maiuscula
    #Mesmo que o usuário digite o nome do produto com letras minusculas, ou todas maiusculas
    # a palavra vai sempre ser formatada com a primeira em maiuscula
    #Geter pega o valar de nome
    @property
    def nome(self):
        return self._nome
    
    #Setter faz a formatação da palavra
    @nome.setter
    def nome(self, valor):
        self._nome = valor.title()              #formata a a palavra para a primeira letra em maiuscula


    #Getter - pega o valor que deseja configura
    @property                                       #decorador para atribução do Getter
    def preco(self):                                #boa prática usar o nome da função com o mesmo nome da variável que deseja configura
        return self._preco                          #boa prática usar o mesmo nome da variavel que deseja configurar com um undescore na frente

    #Setter - configura o valor pego pelo getter, serve para validar algumas situações
    #Exemplo: num cadastro de preços de um produto, o usuário coloca o "R$", onde deveria ter somente numeros
    #com Getter and Setter, isso resolvido, antes do programa processar o valor errado, o Getter e chamado para pegar o valor e 
    # passar para o Setter configurar, assim validando um valor que daria erro
    # Deste modo não há necessidade de mexer na estrutura de código existentes, apenas é adicionado código para fazer a validação
    @preco.setter                                       #decorador do setter deve sempre iniciar com o memso nome da função do getter
    def preco(self, valor):
        if isinstance(valor, str):                      #verifica se é uma str       
            valor = float(valor.replace('R$', ''))      #se for retira o caractere especial e faz um casting para float

        self._preco = valor

p1 = Produto('TRigo', "R$ 10")                     #Sem o getter and setter, o valor de R$ 10,00 daria erro por conta do cifrão

p1.desconto(50)
