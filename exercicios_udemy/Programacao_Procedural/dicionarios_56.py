#o dicionário é semelhante a lista
#lista os itens podem ser acessados pelo numeros dos indices [0], [1]....
#no dicionário é criado um par de chaves, onde o item é acessado pelo nome da chave {'chave':'valor'}
# a chave é o indice do dicionário, a chave tem que ser unica, senão é sobrescrita pelo o ultimo valor atribuido a chave
#a chave pode ser qualquer valor imutável - str, int e tuplas com valores imutáveis (str e Int)

l1 = []
t1 = ()
d1 = {}

print(type(l1))         #lista
print(type(t1))         #tupla
print(type(d1))         #dicionário

print('-----------------------------------------------')

d1 = {
    'str' : 'valor',
    123: 'Outro valor',
    (1,2,3): 'Tupla com valores imultáveis'

}

print(d1[(1,2,3)])                                                      #acessando valor atraves de chaves em tuplas

print('-----------------------------------------------')

d2 = {'chave1':'valor chave 1'}                                         #Criando dicionário e dando valor a chave
d2 ['chave2'] = 'Valor chave 2'                                         #adicionando, acrescentando chave e vale ao dicionário
print(d2)
print(d2['chave1'])                                                      #acessando valor através do nome da chave

d3 = dict(chave3 = 'valor chave 3', chave4 = 'valor chave 4')            #Outra maneira de criar dicionário
print(d3)
print(d3['chave4'])

print('-----------------------------------------------')
#caso seja referenciado uma chave que não existe, vai haver um erro
#exemplo:
#print(d3['chave500'])
#para contornar isso, pode ser feito um if , ou usar o get
#usando if:
if 'chave500' in d3:
    print(d3['chave500'])                   #deste modo o código vai continuar funcionando

#usando .get
print(d3.get('chave500'))                   # usando o get quando a chave não existir vai retornar none ao inves de erro
if (d3.get('chave500')) is not None:        #pode ser usando uma condição juntamente com o get.
    print(d3['chave500'])

print('-----------------------------------------------')
#atualizando o valor da chave
d3['chave3'] = 'Valor chave 3 atualizado'   #valor da chave 3 atualizado (mais utilizado)
print(d3)

print('-----------------------------------------------')
#atualizando usando o update, usado tambem para concatenar dicionários distintos
d3.update({'chave5':'valor chave 5'})                            #novo chave adicionada
d3.update({'chave4':'novo valor para chave 4'})                 #novo chave adicionada
print(d3)

print('-----------------------------------------------')
#apagando chave
del d3['chave3']                #chave 3 deletada
print(d3)

print('-----------------------------------------------')
#verificando se uma chave ou um valor existe no dicionário
print('chave4' in d3)                                           #verifica se a chave4 existe no d3, se sim retorna True, se não False
print('novo valor para chave 4' in d3.values())                 #verifica de o valor existe no dicionario (true ou false)

print('-----------------------------------------------')
#verificando quantos pares existem num dicionário (tamanho do dicionário)
print(len(d3))

print('-----------------------------------------------')
#Iterando sobre um dicionário
for k in d3:                            #acessa as chaves (mostra as chaves)    
    print(k)

for v in d3.values():                   #acessa os valores das chaves (mostra os valores)    
    print(v)

for i in d3.items():                   #acessa os valores das chaves e valores (mostra as chaves e seus valores)  - gera tuplas   
    print(i)

for i in d3.items():                   #acessa os valores das chaves e valores (mostra as chaves e seus valores)  - gera chave e valores separadamente   
    print(i[0], i[1])

for k,v in d3.items():                   #acessa os valores das chaves e valores (mostra as chaves e seus valores)  - desempacotamento   
    print(k,v)

print('-----------------------------------------------')
#Criar cópia real de um dicionário
#import copy
import copy

d5  = {1:'a', 2:'b'}            #dicionário original
d6 = copy.deepcopy(d5)          #faz cópia do dicionário
d6[3] = 'c'                     #inclui novo chave valor no novo dicionário 
print(d5)
print(d6)

print('-----------------------------------------------')
#Conversão de lista em dicionário
lista = [
    ['c1', 1],                  #lista original, deve possuir par de valores para dar certo a conversão
    ['c2', 2],                  #com uma lista de tuplas tambem funciona
    ['c3', 3],                  #com tupla de lista tambem funciona
]

d7 = dict(lista)                #conversão (cast) da lista em dicionário       
print(d7)


print('-----------------------------------------------')
#Exemplo de iteração dupla
#criado um diacionário de clientes, onde cada cliente, possui outro dicionário, com chave e valor
clientes = {
    'cliente1' : {
        'nome' : 'Jacson',
        'sobrenome' : 'Jeremias',
    },
    'cliente2' : {
        'nome' : 'Daiane',
        'sobrenome' : 'Braviano',
    },
} 

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo : {clientes_k}')                   #primeira iteração acessa a chave cliente1, 2 ....
    for dados_k, dados_v in clientes_v.items():        
        print(f'\t{dados_k}, {dados_v}')                #segunda iteração acessa os valores do dicionário da chave 2 que possui os dados do cliente
    
print('-----------------------------------------------')