#Agregação

#Class CarrinhoDeCompras existe serm a classe Produto, mas precisa da classe produto para funcionar perfeitamente
class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []
    
    #Insere um produto que já esta cadastrado na classe Produto
    def inserir_produto(self, produto):
        self.produtos.append(produto)

    #Lista os produtos após inseridos na lista
    def lista_produtos(self):
        i = 0
        for produto in self.produtos:
            i += 1
            print(i, produto.nome, produto.valor)
        print(f'Produtos no carrinho : {float(len(self.produtos))} unidades')

    #Faz a soma após os produtos inseridos na lista
    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        print (f'Valor Total R$ {total}')

#Class Produto, independente de outras classes, mas outras classes dependem dela para funcionar
#Responsável por cadastrar o produto com os valor
#Sem a classe Produto, a classe CarrinhoDeCompras não funciona
class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor