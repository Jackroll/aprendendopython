#Faça um Programa que leia três números e mostre-os em ordem decrescente. 

numeros = []                                                #cria uma lista de numeros 

for i in range (3):                                         #faz a iteração conforme limite definido no range
    valor = float(input(f'Digite o valor {i} : '))          #atribui o valor digitado a variável valor
    numeros.append(valor)                                   #adiciona o valor a lista numeros

numeros.sort(key=int, reverse=True)                         #ordena os valores da lista na ordem decrescente

print(numeros)                                              #mostra a lista



