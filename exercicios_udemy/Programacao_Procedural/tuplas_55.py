#Diferença entre Tupla e lista, a tupla não pode ser editada



t1 = ()             #Tupla ()
l1 = []             #Lista []

print(type(t1))
print(type(l1))

print('-------------------------------------')

t2 = (1,2,3, 'a', 'Jacson')     #A tupla só pode ser editada na sua criação
print(t2)
print(t2[4])                    #itens podem se acessados pelo indíce igual a lista

print('-------------------------------------')

for v in t2:                    #pode ser percorrida atravéz do for igual a lista
    print(v)


print (t2[2:])                  #fatiando a tupla, mostrando a partir do indice 1

print('-------------------------------------')

t3 = 1,2, 'b', 'c'              #Pode ser criada sem os parenteses
print(t3)

t4 = 1,                         #para criar a tupla com 1 elemento deve ser usado uma virgula ao final do item

print('-------------------------------------')

t5 = t3 + t2                    #concatenando tuplas
print(t5)

print('-------------------------------------')

n1, n2, n3, *_, = t5            #desempacotando em variáveis
print(n1, n2, *_)

print('-------------------------------------')

t6 = ('f', 5, 'teste') * 20     #multiplicando tuplas, mostrando 20 vezes a tupla na tela
print(t6)

print('-------------------------------------')

t7 = (1,2,3,4)                  #tupla não pode ter seus valores modificados
t7 = list(t7)                   #Convertendo tupla em list para poder modificar um valor
t7[2] = 5000                    #valor do indice 2 da lista que era uma tupla modificado
print(t7)
t7 = tuple(t7)                  #convertendo lista em tupla novamente
print(t7)

