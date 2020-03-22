#considerando duas listas de inteiros ou floats (lista A e Lista B)
#Some os valores nas listas retornando uma nova lista com os valores somados:
#Se uma lista for maior que a outra, a soma só vai considerar o tamanho da menor
#Exemplo:
#lista_a = [1,2,3,4,5,6,7,8]
#lista_b = [1,2,3,4]
#resultado:
#lista_soma = [2,4,6,8]
from itertools import zip_longest

lista_a = [1,2,3,4,5,6,7,8]
lista_b = [1,2,3,4]

#solução 1 usando zip e a função sum - considera a menor lista para fazer a soma
lista_soma = [sum(v) for v in zip(lista_a, lista_b)]
print(lista_soma)

#solução 2 usando zip, sem usar o sum, apenas somando x e y - considera a menor lista para fazer a soma
lista_soma1 = [x + y for x, y in zip(lista_a, lista_b)]
print(lista_soma1)

#solução 3 usando zip_longest, soma todos os valores não importa o tamanho das lista, o fillvalue atribui um valor
#padrão para os itens faltantes da lista menor 
lista_soma2 = [x + y for x, y in zip_longest(lista_a, lista_b, fillvalue=0)]
print(lista_soma2)