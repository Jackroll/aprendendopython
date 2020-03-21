"""
-> É uma lista de listas de números inteiros
-> As listas internas tem o tamanho de 10 elementos
-> As listas internas contém números entre 1 a 10 e eles podem ser duplicados
Exercício
-> Crie uma função que encontra o primeiro duplicado considerando o segundo
    número como a duplicação. Retorne a duplicação considerada.
        Requisitos:
            A ordem do número duplicado é considerada a partir da segunda
            ocorrência do número, ou seja, o número duplicado em si.
            Exemplo:
                [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
                [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
            Se não encontrar duplicados na lista, retorne -1
"""
lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]




def encontra_primeiro_duplicado (lista):                #função que recebe como parametro uma lista, para encontrar numero duplicado
    numero_checado =set()                               #armazena o numero checado num set
    primeiro_duplicado = -1                             #se não encontrar numero duplicado, valor = -1

    for numero in lista:                                #percorre a lista passada como parametro na função
        if numero in numero_checado:                    #se o numero da lista existir no set numero_checado
            primeiro_duplicado = numero                 #o numero é armazenado na variável primero_duplicado e o sistema e parado
            break

        numero_checado.add(numero)                      #se o numero checado, não existir no set, então ele é adicionado, e continua a iteração
    return primeiro_duplicado                           #se ao final da iteração não for encontrado numero duplicado, retorna -1, caso contrario, retorna o numero encontrado

for l in lista_de_listas_de_inteiros:                   #percorre a lista de listas
    print(l, encontra_primeiro_duplicado(l))            #mostra as listas dentro da lista, e o valor repetido se existir, ou -1 se não exisitir