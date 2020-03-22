"""
Combinations, Permutations and Product
Combinations - combina itens de uma lista entre si- não repetem valores
permutations - combina itens de uma lista leva em consideração a ordem - não repetem valores
product - leva em consideração a ordem e repete valores - usa o parametro repeat para definir a qtd de itens a combinar
"""

from itertools import combinations, permutations, product

pessoas = ['João', 'Arlete', 'Maria', 'Beatriz', 'Aretusa', 'Melania']

#combinando valores de uma lista de 2 em 2 não importanto a ordem
for grupo in combinations(pessoas, 2):          #combinando valores da lista de 2 em 2
    print(grupo)

print('=-'*30)
#permutando valores de uma lista de 2 em 2 leva em consideração a ordem
for grupo1 in permutations(pessoas, 2):          #combina valores com permutation
    print(grupo1)

print('=-'*30)
#combina valores de uma lista conforme repetição especificada, leva em consideração a ordem e repete valores
for grupo2 in product(pessoas, repeat=2):          #combina valores com product
    print(grupo2)
