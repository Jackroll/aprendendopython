from pythonbirds.oo.agregacao.classes import CarrinhoDeCompras, Produto

carrinho = CarrinhoDeCompras()

p1 = Produto('Arroz', 5)
p2 = Produto('Iphone', 11500)
p3 = Produto('Caneca', 5)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p3)

carrinho.lista_produtos()
print(f'Valor Total R$: {carrinho.soma_total()}')