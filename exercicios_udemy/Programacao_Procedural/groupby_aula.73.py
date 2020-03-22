#groupby agrupa itens por alguma condição
#para usar o groupby o item deve estar ordenado
#deve ser importado do itertools

from itertools import groupby, count, tee
#lista a ser ordenada
alunos = [
    {'nome':'Jacson', 'Nota':'A'},
    {'nome':'Pedro', 'Nota':'A'},
    {'nome':'João', 'Nota':'C'},
    {'nome':'Gustavo', 'Nota':'B'},
    {'nome':'Leonardo', 'Nota':'D'},
    {'nome':'Batista', 'Nota':'C'},
    {'nome':'Mandrake', 'Nota':'D'},
    {'nome':'Ruan', 'Nota':'D'},
    {'nome':'Maria', 'Nota':'C'},
    {'nome':'Gorete', 'Nota':'A'},
    {'nome':'Minervina', 'Nota':'D'},
]

#ordenando os dados com a função lambda
ordena = lambda item: item['Nota']
alunos.sort(key = ordena)

#Agrupando os alunos pelas notas
alunos_agrupados = groupby(alunos, ordena)                  #Atraves da expressão lambda agrupa os alunos, informando o agrupamento pela nota

for grupo_notas, notas_agrupadas in alunos_agrupados:       #Acessando o grupo de notas e mostrando A, B, C, D
    print(f'Grupo : {grupo_notas}')                         #mostra os grupos de notas

    v1, v2 = tee(notas_agrupadas)                           #tee cria uma copia do elemento, criando 1 copia e armazenado no V1 e outra no V2

    for nome_aluno in v1:                                   #acessa o nome dos alunos agrupados na nota
        print(f'\t {nome_aluno}')                           #mostra o nome dos alunos agrupados na nota
    total_alunos = len(list(v2))                            #acessa a qtd de alunos agrupados na nota
    print(f'\t Total : {total_alunos} alunos')              #mostra o nome dos alunos agrupados na nota
      
    print('- - '*10)

    