#Exercicio: list comprehension
#Existente - string = '0123456789012345678901234567890123456789012345678901234567890123456789'
#usando list comprehension fazer
#Dividir a string em listas de 10 em 10
#Unir a lista, com ponto a cada 10 numeros
#Saída 1- lista = ['0123456789', '0123456789', '0123456789', '0123456789', '0123456789', '0123456789', '0123456789']
#Saída 2- retorno = 0123456789.0123456789.0123456789.0123456789.0123456789.0123456789.0123456789

string = '0123456789012345678901234567890123456789012345678901234567890123456789'
#método sem usar list comprehension
"""x = int(len(string)/10)
lista = []
for i in range(x):
   lista.append(string[0:10])
print (lista)"""

#meu jeito
lista = [string[0:10] for i in range(int(len(string)/10))]          
retorno = '.'.join(lista)
print(f'{lista}\n{retorno}')

print('******************************************')

#como foi resolvido pelo professor
n = 10
lista1 = [string[i:i+n] for i in range(0, len(string), n)]
retorno1 = '.'.join(lista1)
print(f'{lista1}\n{retorno1}')
