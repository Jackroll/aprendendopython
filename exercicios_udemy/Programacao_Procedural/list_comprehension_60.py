#exemplos de list comprehension

#Multiplicar todos os valores da lista por 2
l1 = [1,2,3,4]
l2 = [v*2 for v in l1]      #faz a iteração em cada elemento da lista multiplicando por 2           
print(l2)

print('=============================================')
#criar tuplas com valores de 0 a 3 para cada valor da lista
l3 = [(v, v2) for v in l1 for v2 in range(3)]       #para cada valor da l1 e feito 3 tuplas com valores de 0 a 3
print(l3)

print('=============================================')
#Substituir vogal a por @ numa lista de strings
l4 = ['maria', 'João', 'banana']
l5 = [v.replace('a', '@') for v in l4]              #para cada letra 'a' encontrado substitui por '@'
print(l5)

print('=============================================')
#acessar e inverter chave e valor de tupla
tupla = (
    ('chave1', 'valor chave1'),
    ('chave2', 'valor chave2'),
)
tupla1 = [(v2, v1) for v1, v2 in tupla]             #valores e chaves invertidos
print(tupla1)
d1 = dict(tupla1)                                   #transformando em dicionário
print(d1)

print('=============================================')
#Usando if e else
l6 = list(range(100))
l7 = [v for v in l6 if v%2 == 0]                    #acessando somente numeros diviseis por 2
print(l7)
print('=============================================')
l8 = [v for v in l6 if v%3 ==0 if v%5 == 0]         #acessando somente numeros diviseis por 3 e 5
print(l8)
print('=============================================')
l9 = [ v if v % 3 ==0 and v % 9 ==0 else 'X' for v in l6]       #numero não divisivel por 3 e 9 coloca 'X'
print(l9)