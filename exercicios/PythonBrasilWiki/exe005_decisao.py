#Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar: 
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#A mensagem "Reprovado", se a média for menor do que sete;
#A mensagem "Aprovado com Distinção", se a média for igual a dez. 

n1 = float(input('Digite a  nota 01 :'))
n2 = float(input('Digite a  nota 02 :'))

media = (n1+n2)/2

if media >=7 and media < 10 :
    print(f'Média : {media} - Aprovado !')
elif media < 7:
    print(f'Média : {media} - Reprovado !')
else :
    print(f'Média : {media} - Aprovado com Distinção !')