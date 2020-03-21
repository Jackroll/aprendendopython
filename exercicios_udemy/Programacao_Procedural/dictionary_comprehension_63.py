#comprehension dictionary

lista = [
    ('ch1', 'valor ch1'),
    ('ch2', 'valor ch2'),
]

print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
#covertendo a lista 1 em dicionário com comprehension
d1 = {c: v for c, v in lista}           #chave : valor para cada chave, valor na lista
print(d1)

print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
#convertendo e passando para maiusculo a chave e o valor
d2 = {c.upper(): v.upper() for c, v in lista}           #convertendo e passando para maiusculo a chave e o valor
print(d2)

print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
#criando dicionário com chave e valor automático com base num range
d3 = {f'ch{x}': x**2 for x in range(5)}
print(d3)