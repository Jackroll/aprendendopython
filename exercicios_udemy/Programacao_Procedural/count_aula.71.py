#count - itertools
#para usar o count, deve ser feito a importação from itertools
#usado para criar um contador para qualquer aplicação


from itertools import count

#contador sem parametros
contador = count()      #contador sem parametros
for v in contador:
    print(v)

    if v >=10:          #definindo limite para o contador, caso contrário fica em loop infinito    
        break

print('=-' * 30)
#contador com parametros
c2 = count(start=5, step=0.1)         #contador com parametro inicial e o valor do passo
for v in c2:
    print(round(v, 2))

    if v >=10:          #definindo limite para o contador, caso contrário fica em loop infinito    
        break

print('=-' * 30)
#Incluíndo indice a uma lista 
lista = ['Jacson', 'João', 'Carlos']
c3 = count()
lista = list(zip(c3, lista))
print(lista)

