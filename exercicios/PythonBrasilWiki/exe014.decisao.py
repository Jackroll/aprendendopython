#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, 
# e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo: 
#Média de Aproveitamento  Conceito
  #Entre 9.0 e 10.0        A
  #Entre 7.5 e 9.0         B
  #Entre 6.0 e 7.5         C
  #Entre 4.0 e 6.0         D
  #Entre 4.0 e zero        E


n1 = float(input('Informe a nota 01 :'))
n2 = float(input('Informe a nota 02 :'))

while (n1 > 10 or n2 > 10) or (n1 <0.5 or n2 < 0.09) :
    print('Valor Inválido ! Digite um valor entre 0 e 10')
    n1 = float(input('Informe a nota 01 :'))
    n2 = float(input('Informe a nota 02 :'))
else :
    media = (n1+n2)/2

    if media >= 9.0 :
        conceito = 'A'
    elif media >= 7.5 :
        conceito = 'B'
    elif media >= 6.0 :
        conceito = 'C'
    elif media >= 4.0 :
        conceito = 'D'
    else :
        conceito = 'E'

if conceito == 'D' or conceito =='E':
        msg = 'REPROVADO'
else :
        msg = 'APROVADO'

print(f'Nota 01 : {n1} \nNota 02 : {n2} \nMédia : {media} \nConceito : {conceito} \nAluno : {msg}')