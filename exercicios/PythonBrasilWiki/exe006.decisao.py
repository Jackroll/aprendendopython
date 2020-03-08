
numeros = int(input('Numero de valores a serem verificados :'))

lista = []

for i in range(numeros) :
    valor = float(input(f'Digite o valor {i} : '))
    lista.append(valor)

lista_ordem = sorted(lista)

print(f'Menor : {lista_ordem[0]} \n Maior : {lista_ordem[len(lista)-1]}')