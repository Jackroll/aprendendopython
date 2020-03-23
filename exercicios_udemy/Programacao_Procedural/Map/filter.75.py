from dados import pessoas, produtos, lista

print('-=' * 30)
#filtrando itens maiores que 5 com o filter
nova_lista = filter(lambda x: x > 5, lista)
print(nova_lista)

print('-=' * 30)
#filtrando atravéz do list comprehension
nova_lista1 = [v for v in lista if v > 5]
print(nova_lista1)

print('-=' * 30)
#filtrando itens maior que 50 na lista de produtos
novo_produto = filter(lambda p: p['preco'] > 50, produtos)
for produto in novo_produto:
    print(produto)

print('-=' * 30)
#filtrando itens maior que 100 na lista de produtos com função
def filtra(produto):
    if produto['preco'] > 100:
        return True
novo_produto1 = filter(filtra, produtos)
for produto1 in novo_produto1:
    print(produto1)

print('-=' * 30)
#filtrando pessoas maior de 18 anos na lista de pessoas
def filtra_idade(idade):
    if idade['idade'] > 18:
        idade['Maior de idade'] = True
    return True
novo_pessoas = filter(filtra_idade, pessoas)
for p in novo_pessoas:
    print(p)