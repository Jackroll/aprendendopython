#map - usado para fazer mapeamento de dados
#o primeiro argumento é sempre uma função, pode ser usado a expressão lambda
from dados import produtos, pessoas, lista

print('-=' * 30)
#map com lista
nova_lista = map(lambda x: x * 2, lista)
print(list(nova_lista))

print('-=' * 30)
#resolvido o caso anterior com list comprehension
nova_lista2 = [(v*2)for v in lista]
print(nova_lista2)

print('-=' * 30)
#map com dicionários
#retornar apenas os preços do dicionario produtos
precos = map(lambda p: p['preco'], produtos)        #para um preço 'p', acessa 'p' na chave 'preco', no dicionário produtos      

for preco in precos:
    print(preco)

print('-=' * 30)
#aumentar preços

#função para aumentar o preço
def aumenta_precos(p1):
    p1['preco'] = round(p1['preco'] * 1.05,2)
    return p1

produtos_novos_precos = map(aumenta_precos , produtos)           #Atualiza os preços do dicionário
precos = map(lambda p: p['preco'], produtos_novos_precos)       #filtra apenas a coluna preços para mostrar na tela
for preco in precos:
    print(preco)

print('-=' * 30)                                                #mostrando lista completa                       
for produto in produtos:
    print(f'\t{produto}')

#mostrando somente os nomes na lista pessoas atraves do lambda
print('-=' * 30)
nomes = map(lambda n: n['nome'], pessoas)
for n in nomes:
    print(n)

#Criar novo campo da lista de pessoas
#função para criar nova chave:valor
print('-=' * 30)
def nova_idade (p):
    p['nova_idade'] = round(p['idade'] * 1,20)  
    return p
pessoas = map(nova_idade, pessoas)          #função usada no map

for p in pessoas:
    print(p)