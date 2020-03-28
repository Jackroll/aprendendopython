"""
Agregação:
Uma classe existe sem a outra, no entanto uma depende da outra para o correto funcionamento, uma classe depende da outra
"""

from classes import CarrinhoDeCompras, Produto

#Instancia a Classe CarrinhoDeCompras
carrinho = CarrinhoDeCompras()

#cadastra os produtos Classe Produto
p1 = Produto('Feijão', 2.50)
p2 = Produto('Abacate', 2.00)
p3 = Produto('Uva', 5.50)

#Insere os produtos no carrinho de compras
carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)

#Lista os produtos do carrinho de compras
carrinho.lista_produtos()

#Soma o valor dos produtos do carrinho de compras.
carrinho.soma_total()