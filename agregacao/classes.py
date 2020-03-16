""" Agregação é quando uma classe pode existir sozinha, no entanto ela depende de outra classe para funcionar corretamente
por exemplo: A Classe 'Carrinho de compras' pode existir sózinha, mas depende da classe 'Produtos' para pode funcionar corretamente
pois seus métodos dependem da classe produto.
E classe Produtos por sua vez existe sozinha e não depende em nada da classe Carrinho de compras
"""

class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def inserir_produto(self, produto):
        self.produtos.append(produto)

    def lista_produtos(self):
        i = 0
        for produto in self.produtos:
            i = i+1
            print(f'Item : {i} - {produto.nome}  R$ {produto.valor}')

    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return total


class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor
