from dados import produtos, pessoas, lista
from functools import reduce

print('-='*20)
#fazendo um reduce manualmente
acumula = 0
for item in lista:
    acumula += item

print(acumula)

print('-='*20)
#usando reduce
soma_lista = reduce(lambda  ac, i: i + ac, lista, 0)     #a iteração é feita somando 'i' com 0 (valor inicial) e guardado e somado com o 'ac' acumulador
print(soma_lista)

print('-='*20)
#somando preços do dicionário
soma_precos = reduce(lambda ac, p: round(p['preco'] + ac,2) , produtos, 0)
print(f'Valor total dos produtos R$ {soma_precos}')

print('-='*20)
#vendo a média das idades
soma_idade = reduce(lambda ac, i: i['idade'] + ac, pessoas,0)       #encontra a soma da idade
print(f'Média de idade: {soma_idade / len(pessoas)}')                                    #mostrando a média