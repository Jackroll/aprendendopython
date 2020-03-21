#Sets ou conjuntos são semelhantes ao dicionário, no entanto sem o par chave : valor
#sets recebem apenas valores unicos
#como se fossem tuplas entre chaves --> { 1,2,3,4}
#suportam valores imutáveis int, str e tuplas
#não tem indice, logo não da de acessar um item pelo numero de indice
#sets não aceitam elementos repetidos
#util para eliminar elementos duplicados de uma lista

l1 = []
t1 = ()
d1 = {}
s1 = {1}        #cria set com valor 1
s2 = set()      #cria set vazio

print(type(l1))
print(type(t1))
print(type(d1))
print(type(s1))

print('---------------------------')

#criando set vazio
s3 = set()
#adicionando (add) valores
s3.add(1)          
s3.add((14,8, 'Jacson'))        #adicionando tupla
#removendo (discard) valor
s3.discard((1))
#adicionando (update) elementos com update
s3.update('teste')                  #update adiciona apenas elementos iteraveis, como str, se incluir uma palavra, vai ser inserido cada letra separadamente
                                    #as letras repetidas são adicionadas uma unica vez e em qualquer ordem

s3.update((12,15,16), [25,31,78], {45,12,18,12})
print(s3)

print('---------------------------')
#removendo elementos duplicados de uma lista
l1 = [1,2,3,3,3,3,3,3, 'pedro', 'pedro', 'pedro']       
l1 = set(l1)                                            #casting para remover itens duplicados
l1 = list(l1)                                           #casting para voltar a ser uma lista                                        
print(l1)

print('---------------------------')
#unindo (union | )sets diferentes, une dois sets com apenas um item de cada valor
s4 = set((12,18,25,'Jacson'))
s5 = s4.union(s3)                           
s6 = s5 | s4
print(s6)

print('---------------------------')
#Intersecção (intersection &) - elementos presentes nos dois sets
s7 = s4 & s6
print(s7)

print('---------------------------')
#Diferença (difference (-)), importante elementos do set da esquerda
s8 = set((1,2,3,4))
s9 = set( (1,2,3,9,10))
s10 = s8 - s9                       #vai mostrar apenas o 4, pois é o unico elemento diferente no set da esquerda com relação ao set da direita
print(s10)                          #se inverter a posição s9 - s8, vai mostrar o 9 e 10

print('---------------------------')
#Diferença simetrica (symmetric_difference (^)), elementos que estão nos dois sets, mas não em ambos ao mesmo tempo
s11 = s8 ^ s9                       #vai mostrar o 4, 9 e 10
print(s11)